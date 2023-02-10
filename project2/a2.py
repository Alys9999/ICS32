import pathlib as p
import Profile
import ds_client as dsc

def process():
    """all"""
    while True:
        i=inputa()
        if i[0]in ("C","R","O"):
            a=decideCRO(i)
            if i[0]=="O" and a!=None:
                return a
        else:
            
            print("invalid command")
    
def inputa():
    """take a valid input"""
    while True:
        first=input()
        if first:
            com0=first[0]
            i=first.find("-n")
            com1=""
            path=""
            filename=""
            if i != -1:
                com1=first[i:i+2]
                try:
                    path=first[2:i-1]
                    filename=first[i+3:]
                except IndexError:
                    print("invalid input")
                    pass
            if path=="":
                path=first[2:]
            lis=[com0,path,com1,filename]
            break
        else:
            print("invalid input")
            pass
    lis2=[]
    for i in lis:
        if i:
            lis2.append(i)
            
    return lis2

def pa(flist:list):
    """get path"""
    if len(flist)>=2:
        path=p.Path(flist[1])
        return path
    else:
        print("2")
        retry()

        

def validdir(path):
    """valid directory"""
    if path.exists() and path.is_dir():
        return True
    else:
        return False
    

def validfile(path):
    """valid file"""
    if path.exists() and path.is_file():
        return True
    else:
        return False



def decideCRO(flist:list)->list:
    """take input and decide L Q C D R"""
    path=pa(flist)
    if flist[0]=="C":
        if validdir(path):
            if flist[2]=="-n": 
                try:
                    ifC(flist,path)
                except FileExistsError:
                    print("file already exists")
            else:
                print("command -n missed")
        else:
            print("invalid path")
    elif flist[0]=="R":
        if validfile(path):
            if path.suffix==".dsu":
                ifR(flist)
            else:
                print("not a .dsu file")
        else:
            print("invalid path")
    elif flist[0]=="O":
        if validfile(path):
            if path.suffix==".dsu":
                return ifO(flist)
            else:             
                print("not a .dsu file")
        else:
            print("invalid path")
            
def valid_un():
    """take valid username"""
    while True:
        username=input("username: ")
        if username:
            return username
        else:
            print("invalid username")
            
def valid_pw():
    """take valid password"""
    while True:
        password=input("password: ")
        if password:
            return password
        else:
            print("invalid password")

def ifC(p:list,path):
    """create a file with wanted name and adding information to it"""
    na=p[3]+".dsu"
    path=pa(p)
    path=path.joinpath(na)
    f=open(path,"x")
    print("Create your profile Information\n")
    dsuserver=valid_server()
    username=valid_un()
    password=valid_pw()
    profile=Profile.Profile(dsuserver=dsuserver,username=username,password=password)
    profile.save_profile(path)
    print("infomation added")
    f.close()


def ifR(p:list)->list:
    """read contend of the determined file"""
    path=pa(p)
    file=path.open()
    contend=file.read()
    if not contend:
        q="EMPTY"
    else:
        p=contend.strip()
        print(p)
    file.close()


def ifO(p:list)->list:
    """load the file"""
    str_path=str(pa(p))
    profile=Profile.Profile()
    profile.load_profile(str_path)
    '''dsuserver=str(profile.dsuserver)
    password=str(profile.password)
    username=str(profile.username)
    bio=str(profile.bio)
    posts=(profile._posts)
    loaded_list=[dsuserver,username,password,bio,posts]'''
    return profile



'UI'

def have_para_by_file():
    """inform user how to operate and process the file"""
    print("R [path]   for readlines")
    print("C [path} -n [filename]    for create new file and saving the profile")
    print("O [path] for loading the profile")
    return process()

def valid_com():
    """take valid command"""
    while True:
        com=input()
        if com=="Yes" or com=="No":
            return com
        else:
            print("Please type in Yes or No")
            
def valid_server():
    """take valid server"""
    while True:
        server=input("ip:port: ")
        if server.find(":")==server.rfind(":")!=-1:
            return server
        else:
            print("Please type in ip:port")
            
def sent(server:str, port:int, username:str, password:str, message:str=None, bio:str=None):
    """the send operation"""
    try:
        soc=dsc.connect(server,port)
        print("connected")
    except Exception as ex:
        print("connection failed")
        return ex
    token=''
    j_obj=dsc.join(soc,username,password,token)
    if j_obj['response']['type']=="ok":
        token=j_obj['response']["token"]
        print("join success")
        if message!=None:
            p_obj=dsc.sMes(soc,token,message)
            if p_obj['response']["type"]=="ok":
                print("post success")
            elif p_obj['response']["type"]=="error":
                bug=p_obj['response']["message"]
                print(bug)
        if bio!=None:
            b_obj=dsc.sBio(soc,token,bio)
            if b_obj['response']["type"]=="ok":
                print("bio sent")
            elif b_obj['response']["type"]=="error":
                bug=b_obj['response']["message"]
                print(bug)
    elif j_obj['response']["type"]=="error":
        bug=j_obj['response']["message"]
        print(bug)
    soc.close()

    
            
def main():
    """the main UI procedure"""
    print("Welcome to the Distrubuted Social")
    print("-----------------------------------")
    print("Please specify you server user name and password")
    profile=have_para_by_file()
    server=profile.dsuserver
    username=profile.username
    password=profile.password
    s_list=server.split(":")
    ip=s_list[0]
    port=s_list[1]
    port=int(port)
    while True:
        
        message=input("message: ")
        print("Do you want to add bio? Yes or No")
        ifbio=valid_com()
        if ifbio=="Yes":
            bio=input("your bio: ")
            sent(ip,port,username,password,message,bio)
            profile.bio=bio
        else:
            sent(ip,port,username,password,message)
        post=Profile.Post(message)
        profile.add_post(post)
        print("keep working? Yes or No")
        ifwork=valid_com()
        if ifwork=="Yes":
            pass
        elif ifwork=="No":
            break
    
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
