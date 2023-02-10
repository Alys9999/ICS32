#Zhaoyang Lu
#zhaoyal5@ci.edu
#30735594
import json
import time



'in json format'
'''# join as existing or new user
{"join": {"username": "ohhimark","password": "password123","token":"user_token"}}

# time.time() function
{"token":"user_token", "post": {"entry": "Hello World!","timestamp": "1603167689.3928561"}}

# for bio, you will have to generate the timestamp yourself or leave it empty.
{"token":"user_token", "bio": {"entry": "Hello World!","timestamp": "1603167689.3928561"}}'''


def join(username: str,password: str,token:str):
    join=json.dumps({"join": {"username": username,"password": password,"token":token}},separators=(",",":"))
    return join

def post(token:str,entry:str):
    timestamp=time.time()
    post=json.dumps({"token": token, "post": {"entry": entry,"timestamp":timestamp}},separators=(",",":"))
    return post

def bio(token:str,entry:str):
    timestamp=time.time()
    bio=json.dumps({"token":token, "bio": {"entry": entry,"timestamp": timestamp}},separators=(",",":"))
    return bio

def send_mes(token:str, entry: str, recipient: str):
    timestamp=time.time()
    send_Mes=json.dumps({'token': token, 'directmessage': {'entry': entry, 'recipient': recipient, 'timestamp': timestamp}},separators=(",",":"))
    return send_Mes

def req_unread(token: str):
    req_Unread=json.dumps({'token': token, 'directmessage': 'new'},separators=(",",":"))
    return req_Unread
    
def all_mess(token: str):
    all_Mess=json.dumps({'token': token, 'directmessage': 'all'},separators=(",",":"))
    return all_Mess
    
    