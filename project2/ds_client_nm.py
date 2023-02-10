import socket
import ds_protocol as dsp
import json


def connect(host:str,port:int):
    A=(host,port)
    soc=socket.socket()
    soc.connect(A)
    print("connected!")
    return soc


def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
    soc=connect(server,port)
    token=''
    j=dsp.join(username,password,token)
    sent=soc.makefile('w')
    sent.write(j)
    sent.flush()
    j_data=soc.makefile('r')
    j_mes=j_data.readline()
    j_obj = json.loads(j_mes)
    if j_obj['response']['type']=="ok":
        print("join success")
        token=j_obj['response']["token"]
        p=dsp.post(token,message)
        sent.write(p)
        sent.flush()
        p_data=soc.makefile('r')
        p_mes=p_data.readline()
        p_obj = json.loads(p_mes)
        if p_obj['response']['type']=="ok":
            print("message sent")
        elif p_obj['response']["type"]=="error":
            bug=p_obj['response']["message"]
            print(bug)
        if bio!=None:
            b=dsp.bio(token,bio)
            sent.write(b)
            sent.flush()
            b_data=soc.makefile('r')
            b_mes=b_data.readline()
            b_obj = json.loads(b_mes)
            if b_obj['response']['type']=="ok":
                print("bio sent")
            elif b_obj['response']["type"]=="error":
                bug=b_obj['response']["message"]
                print(bug)
    elif j_obj['response']["type"]=="error":
        bug=j_obj['response']["message"]
        print(bug)
    soc.close()
    

    

a=send("168.235.86.101",2021,"user","123","mess","hhhh")







