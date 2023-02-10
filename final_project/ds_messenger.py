import time
import ds_protocol as dsp
import socket
import json

class DirectMessage(dict):

    def __init__(self,sender=None,recipient=None, message=None,timestamp:float=0.0):
        self.sender=sender
        self.recipient = recipient
        self.message = message
        self.message_pair_list=[]
        self.timestamp=timestamp
        dict.__init__(self, sender=self.sender, entry=self.message, recipient=self.recipient, timestamp=self.timestamp)
        
        
    
    def sortMes(self):
        self.messages_pair_list=sorted(self.messages_pair_list, key=lambda i: i['timestamp'])



class DirectMessenger:
    def __init__(self, dsuserver='168.235.86.101', username='test_user999', password='pw'):
        self.token = ''
        #current user
        self.dsuserver=dsuserver
        self.username=username
        self.password=password
        #a list of dict object pairing friends and theri coresponding chats
        self._friend_message=[]
        #a list of friends
        self.friends_list=[]
        self.all_list=[]
        self.pairing_list=[]
        #making the connection
        A=(self.dsuserver,2021)
        soc=socket.socket()
        soc.connect(A)
        self.soc=soc
        
        #reset the user info when trying to change the account
    def renew_info(self,dsuserver,username,password):
        self.dsuserver=dsuserver
        self.username=username
        self.password=password
        self._friend_message=[]
        self.friends_list=[]
        self.all_list=[]
        self.pairing_list=[]
        A=(self.dsuserver,2021)
        soc=socket.socket()
        soc.connect(A)
        self.soc=soc
        
        

    def join(self):
        """send a join command"""
        soc=self.soc
        j=dsp.join(self.username,self.password,self.token)
        sent=soc.makefile('w')
        sent.write(j)
        sent.flush()
        j_data=soc.makefile('r')
        j_mes=j_data.readline()
        j_obj = json.loads(j_mes)
        if j_obj['response']['type']=='ok':            
            self.token=j_obj['response']['token']
            return 1
        elif j_obj['response']['type']=='error':
            return j_obj['response']['message']
    
    def send(self, entry, recipient) -> bool:
        # returns true if message successfully sent, false if send failed.
        token=self.token
        mes=dsp.send_mes(token, entry, recipient)
        sent=self.soc.makefile('w')
        sent.write(mes)
        sent.flush()
        p_data=self.soc.makefile('r')
        p_mes=p_data.readline()
        p_obj = json.loads(p_mes)
        if p_obj['response']['type']=='ok':
            return True
        else:
            return False
     
    def retrieve_new(self) -> list:
        # returns a list of DirectMessage objects containing all new messages
        mes=dsp.req_unread(self.token)
        sent=self.soc.makefile('w')
        sent.write(mes)
        sent.flush()
        p_data=self.soc.makefile('r')
        p_mes=p_data.readline()
        p_obj = json.loads(p_mes)
        if p_obj['response']['type']=='ok':
            for x in p_obj['response']['messages']:
                dm=DirectMessage(x['from'], self.username, x['message'],x['timestamp'])
                self._friend_message.append(dm)
            return self._friend_message
        else:
            return False

    def retrieve_all(self) -> list:
        # returns a list of DirectMessage objects containing all messages
        mes=dsp.all_mess(self.token)
        sent=self.soc.makefile('w')
        sent.write(mes)
        sent.flush()
        p_data=self.soc.makefile('r')
        p_mes=p_data.readline()
        self.p_obj = json.loads(p_mes)
        #info recieved from server
        if self.p_obj['response']['type']=='ok':
            for x in self.p_obj['response']['messages']:
                dm=DirectMessage(x['from'], self.username, x['message'],x['timestamp'])
                self._friend_message.append(dm)
                #take info from server to DirectMessage and apppend it to _friend_message
            return self._friend_message
        else:
            return False
        
    def make_pair(self):
        same_chat_list=[]
        self.pairing_dict={}
        for x in self._friend_message:
            if x['sender'] not in self.friends_list:
                #find all friends chat and store them in friends_list
                self.friends_list.append(x['sender'])
        for y in self.friends_list:
            for i in self._friend_message:
                if y==i['sender']:
                    #find the corresponding messages of the friend and store these info together
                    same_chat_list.append(i)
            same_chat_list=sorted(same_chat_list, key=lambda i: str(i['timestamp']),reverse=True)
            #make a dict of the friend chat and the friend chat info
            self.pairing_dict[y]=same_chat_list
            same_chat_list=[]






            

        
        
        
        
        
        
