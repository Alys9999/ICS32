from ds_messenger import DirectMessenger

# create a DirectMessenger
# parameter: server ip, username, password
ds = DirectMessenger("168.235.86.101","username","password")

# send a message to a specific user
# parameter: message content,recipient name
# return: true or false
status = ds.send("message content","Joy")
if status:
    print("send direct message success!")
else:
    print("send direct message fail!")

# Request unread message from the DS server sent to current user
# no parameter
# return a list of DirectMessage
messages = ds.retrieve_new()

for message in messages:
    print(message.recipient) # 消息发送者
    print(message.message) # 消息内容
    print(message.timestamp) #消息发送时间

# Request all message from the DS server send to current user
# no parameter
# return a list of DirectMessage, similar to retrieve_new()
messages = ds.retrieve_all()