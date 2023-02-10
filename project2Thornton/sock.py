import socket
import time


'''connect, read, write
'''
            
def connect():
    myname = socket.gethostname()
    #获取本机ip
    myPC_IP = socket.gethostbyname(myname)
    host=myPC_IP
    '''input("Host:")'''
    port=8888
    '''input("Port")'''
    A=(host,port)
    soc=socket.socket()
    soc.connect(A)
    print("connected!")
    return soc

            
            
def send(soc,txt):
    soc.send(txt.encode('utf-8'))

        
    
def rec(soc):
    data = soc.recv(1024)
    data=data.decode('utf-8')
    print(data)
    return data
        
            
            

    
        
