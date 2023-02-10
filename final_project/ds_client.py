#Zhaoyang Lu
#zhaoyal5@ci.edu
#30735594
import socket
import ds_protocol as dsp
import json


def connect(host:str,port:int):
    """make connection"""
    A=(host,port)
    soc=socket.socket()
    soc.connect(A)
    return soc

def join(soc,username,password,token):
    """send a join command"""
    j=dsp.join(username,password,token)
    sent=soc.makefile('w')
    sent.write(j)
    sent.flush()
    j_data=soc.makefile('r')
    j_mes=j_data.readline()
    j_obj = json.loads(j_mes)
    return j_obj

def sMes(soc,token,message):
    """send a message"""
    p=dsp.post(token,message)
    sent=soc.makefile('w')
    sent.write(p)
    sent.flush()
    p_data=soc.makefile('r')
    p_mes=p_data.readline()
    p_obj = json.loads(p_mes)
    return p_obj

def sBio(soc,token,bio):
    """send a bio"""
    b=dsp.bio(token,bio)
    sent=soc.makefile('w')
    sent.write(b)
    sent.flush()
    b_data=soc.makefile('r')
    b_mes=b_data.readline()
    b_obj = json.loads(b_mes)
    return b_obj


def send(server:str, port:int, username:str, password:str, message:str=None, bio:str=None):
    """the send operation"""
    try:
        soc=connect(server,port)
    except Exception as ex:
        err='connnection failed due to\n' + str(ex)
        return err
    token=''
    j_obj=join(soc,username,password,token)
    if j_obj['response']['type']=="ok":
        token=j_obj['response']["token"]
        if message!=None:
            p_obj=sMes(soc,token,message)
            if p_obj['response']["type"]=="error":
                bug=p_obj['response']["message"]
                return bug
        if bio!=None:
            b_obj=sBio(soc,token,bio)
            if b_obj['response']["type"]=="error":
                bug=b_obj['response']["message"]
                return bug
    elif j_obj['response']["type"]=="error":
        bug=j_obj['response']["message"]
        return bug
    soc.close()

    

    






