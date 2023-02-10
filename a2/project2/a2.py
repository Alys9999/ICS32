import pathlib as p
import Profile
import ds_client as dsc

def process():
    'all'
    while True:
        i=inputa()
        if i[0]in ("Q","L","C","D","R","O"):
            a=decideQLCDRO(i)
            if len(i)>2 and i[2]=="-r":
                b=decide_r(i,a)
                if len(i)>3 and (i[3] in ("-s", "-f", "-e")):
                    d=decide_sfe(i,b)
                    ltp(d)
                    pass
                else:
                    ltp(b)
                    pass
            elif len(i)>2 and (i[2] in ("-s","-f","-e")):
                c=decide_sfe(i,a)
                ltp(c)
            else:
                if i[0]=="O":
                    return a 
                else:
                    ltp(a)
                    pass
        else:
            retry()

    
def retry():
    'retry everything'
    print("ERROR")
    process()
    

def inputa():
    'take a valid input'
    first=input()
    try:
        com0=first[0]
    except IndexError:
        return False
    c=["-r","-s", "-f", "-e",  "-n"]
    path=""
    com1=""
    com2=""
    filename=""
    for x in c:
        if first.find(x) !=-1:
            c1=first.find(x)
            com1=x
            path=first[2:c1-1]
            c.remove(x)
            for y in c:
                if first.find(y)!=-1:
                    c2=first.find(y)
                    com2=y
                    filename=first[c2+3:]
                    break
            if filename=="":
                filename=first[c1+3:]
            break
    if path=="":
        path=first[2:]
    lis=[com0,path,com1,com2,filename]
    for i in lis:
        if i=="":
            lis.remove(i)
    return lis

def pa(flist:list):
    'get path'
    if len(flist)>=2:
        path=p.Path(flist[1])
        return path
    else:
        retry()

def ltp(oal):
    '''transform list to path'''
    if type(oal) is list:
        for x in oal:
            print (x)
    else:
        print(oal)

        
'valid directory'
def validdir(path):
    'valid directory'
    if path.exists() and path.is_dir():
        return True
    else:
        return False
    
'valid file'
def validfile(path):
    'valid file'
    if path.exists() and path.is_file():
        return True
    else:
        return False



def decideQLCDRO(flist:list)->list:
    'take input and decide L Q C D R'
    path=pa(flist)
    if flist[0]=="Q":
        print("Closed")
        return ""
    elif flist[0]=="L" and validdir(path):
        '''if it exist and is a directory'''
        return ifLr(path,0)
    elif flist[0]=="C" and validdir(path) and flist[2]=="-n":
        return ifC(flist)
    elif flist[0]=="D" and validfile(path):
        return ifD(flist)
    elif flist[0]=="R" and validfile(path) and path.suffix==".dsu":
        return ifR(flist)
    elif flist[0]=="O" and validfile(path) and path.suffix==".dsu":
        return ifO(flist)
    else:
        retry()

        

def decide_r(flist:list,lf:list):
    'make decision of r'
    repath=pa(flist)
    rf=ifLr(repath,1)
    return rf

        
        
        

def decide_sfe(flist:list,rf:list)->list:
    'make decisions of sfe'
    if "-f" in flist:
        return iff(rf)
    elif "-e" in flist:
        for x in range(len(flist)-1):
            if flist[x]=="-e":
                try:
                    su=flist[x+1]
                except IndexError:
                    retry()
        return ife(su,rf)
    elif "-s" in flist:
        for x in range(len(flist)-1):
            if flist[x]=="-s":
                try:
                    na=flist[x+1]
                except IndexError:
                    retry()
        return ifs(na,rf)
    else:
        return rf
    

        
' cases '

        


def ifLr(p,r:int)->list:
    'return files in the dirctory'
    od=[]
    of=[]
    for x in p.iterdir():
        if x.is_dir():
            od.append(x)
            od.sort()
            if r==1:
                for i in (ifr(x)):
                    od.append(i) 
        else:
            of.append(x)
            of.sort()
    of.extend(od)
    return of


def iff(li:list)->list:
    'return all not dir in the list'
    fl=[]
    for x in li:
        if x.is_file():
            fl.append(x)
    return fl


def ifs(na:str,li:list)->list:
    'return file with wanted name'
    fl=[]
    for x in li:
        if x.name==na:
            fl.append(x)
    return fl

def ife(su:str,li:list)->list:
    'return file with wanted suffix'
    fl=[]
    su="."+su
    for x in li:
        if x.suffix==su:
            fl.append(x)
    return fl

def ifC(p:list):
    'create a file with wanted name'
    na=p[3]+".dsu"
    path=pa(p)
    path=path.joinpath(na)
    f=open(path,"x")
    ifinfo=input("Any Information? Yes or No\n")
    if ifinfo=="Yes":
        dsuserver=input("server: ")
        username=input("username: ")
        password=input("password")
        profile=Profile.Profile(dsuserver=dsuserver,username=username,password=password)
        profile.save_profile(profile)
        print("infomation added")
    else:
        pass
    f.close()
    return path
    
def ifD(p:list)->str:
    'delete the determined file'
    path=pa(p)
    path.unlink()
    d=str(path)+" DELETED"
    return d

def ifR(p:list)->list:
    'read contend of the determined file'
    path=pa(p)
    file=path.open()
    contend=file.read()
    if not contend:
        q="EMPTY"
    else:
        p=contend.strip()
        q=[p]
    file.close()
    return(q)

def ifO(p:list)->list:
    str_path=str(pa(p))
    profile=Profile.Profile()
    profile.load_profile(str_path)
    dsuserver=str(profile.dsuserver)
    password=str(profile.password)
    username=str(profile.username)
    bio=str(profile.bio)
    posts=(profile._posts)
    loaded_list=[dsuserver,username,password,bio,posts]
    return loaded_list



'UI'
def fileSystem():
    print("   These is how to find your proflie:")
    print("your input should be in the form of [command1][path][command2][command3][filename or suffix]")
    print("command3 is optional, every object should be sparated by space")
    print("Q: quit, L C D R O")
    print("-r")
    print("-s,-f,-e")
    
def have_para_by_file():
    fileSystem()
    return process()

def valid_com():
    while True:
        com=input()
        if com=="Yes" or com=="No":
            return com
        else:
            print("Please type in Yes or No")
            
def valid_server():
    while True:
        server=input("ip:port: ")
        if server.find(":")==server.rfind(":")!=-1:
            return server
        else:
            print("Please type in ip:port")
            
    

def main():
    print("Welcome to the Distrubuted Social")
    print("-----------------------------------")
    print("Please specify you server user name and password")
    print("do you want to load your profile? Yes or No")
    com=valid_com()
    if com=="Yes":
        loaded_list=have_para_by_file()
        server=loaded_list[0]
        username=loaded_list[1]
        password=loaded_list[2]
    elif com=="No":
        server=valid_server()
        username=input("username: ")
        password=input("password: ")
    s_list=server.split(":")
    ip=s_list[0]
    port=s_list[1]
    port=int(port)
    message=input("message: ")
    print("Do you want to add bio? Yes or No")
    ifbio=valid_com()
    if ifbio=="Yes":
        bio=input("your bio: ")
        dsc.send(ip,port,username,password,message,bio)
        profile=Profile.Profile(server,username,password)
        profile.bio=bio
    else:
        dsc.send(ip,port,username,password,message)
        profile=Profile.Profile(server,username,password)
    post=Profile.Post(message)
    profile.add_post(post)
    
    print("Please type in the path you want to save your work")
    while True:
        path=p.Path(input())
        if validfile(path) and path.suffix==".dsu":
            profile.save_profile(path)
            break
        else:
            print("invalid path")
    print("profile saved")
    



    
  
if __name__ == '__main__':
    
    main()
