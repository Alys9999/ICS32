import sock as s
import CommonLib as C
import ConnectFour as CF
#username
#build a new board and send the r and c
#read and give command




def m():
    print("welcome to the CF online version, please input host and port")
    estcon=s.connect()#maka the connection
    a=uname()
    s.send(estcon,a)#send username
    data=s.rec(estcon)
    print("here is your game")
    col=C.col0()
    row=C.row0()
    ag="AI_GAME "+str(col)+" "+str(row)
    print(ag)
    s.send(estcon,ag)
    nb=C.F(col,row)
    while True:
        co=C.dpn()
        s.send(estcon,co)
        nb=C.proc(nb,co)
        if CF.winner(nb)!=0:
            a=C.we(nb)
            print(a)
            s.send(estcon,a)
            return 0
        data=s.rec(estcon)
        nb=C.proc(nb,data)
        
    estcon.close()
    
    
'''启动，
    c输入，
    发送
    生成
    接收（s输入）
    生成
    c输入
'''
    
    
def uname():
    username=input("please type in your username:")
    servertype=str("I32CFSP_HELLO ")
    s=servertype+username
    return s

        
if __name__=="__main__":
    m()


