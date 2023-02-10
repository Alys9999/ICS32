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