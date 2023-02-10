import socket
import CommonLib as C
import ConnectFour as CF
import sock as s


def soc():
    #获取本机电脑名
    myname = socket.gethostname()
    #获取本机ip
    myPC_IP = socket.gethostbyname(myname)
    A = (myPC_IP, 8888)
    tcpS = socket.socket()  # 创建socket对象
    #避免TIME_WAIT占用port 导致出错
    tcpS.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    #加入socket配置，重用ip和端口
    tcpS.bind(A) # 绑定ip端口号
    tcpS.listen(5)  # 设置最大链接数
    while True:
        print("服务器启动，监听客户端链接")
        clientsocket, addr = tcpS.accept() 
        print("链接的客户端 ", addr)
        while True:
            try:
                uname=clientsocket.recv(4096)
                a=unamechange(uname)
                se=str("Welcome "+a[1])
                clientsocket.send(se.encode("utf-8"))
                gametype=clientsocket.recv(4096)
                a=gametypechange(gametype)
                col=int(a[1])
                row=int(a[2])
                nb=C.F(col,row)
                while True:
                    '''接收（c输入），生成，s输入，发送，生成，接收（c输入）'''
                    data=s.rec(clientsocket)
                    nb=C.proc(nb,data)
                    if CF.winner(nb)!=0:
                        a=C.we(nb)
                        print(a)
                        s.send(clientsocket,a)
                        clientsocket.close()
                    else:
                        co=C.dpn()
                        s.send(clientsocket,co)
                        nb=C.proc(nb,co)
                    
            except ConnectionResetError:
                print("using connection turned off")
                break


    
    
def unamechange(uname):
    a=str(uname.decode("utf-8"))
    a=a.split()
    if a[0]=="I32CFSP_HELLO":
        return a
    
def gametypechange(gametype):
    a=str(gametype.decode("utf-8"))
    a=a.split()
    if a[0]=="AI_GAME":
        return a
    
'''a="AI_GAME 5 6"
print(gametypechange(a.encode("utf-8")))'''
    
          
    
    
    

if __name__=="__main__":
    soc()
