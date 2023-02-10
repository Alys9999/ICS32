import pathlib as p
import Profile
import ds_client as dsc

def process():
    """all"""
    while True:
        i=inputa()
        if i[0]in ("C","R","O"):
            a=decideCRO(i)
            if i[0]=="O":
                return a
        else:
            print("invalid command")
    
def inputa():
    'take a valid input'
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
    'get path'
    if len(flist)>=2:
        path=p.Path(flist[1])
        return path
    else:
        print("2")
        retry()

        
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



def decideCRO(flist:list)->list:
    'take input and decide L Q C D R'
    path=pa(flist)
    if flist[0]=="C" and validdir(path) and flist[2]=="-n":
        try:
            ifC(flist,path)
        except FileExistsError:
            print("file already exists")
    elif flist[0]=="R" and validfile(path) and path.suffix==".dsu":
        ifR(flist)
    elif flist[0]=="O" and validfile(path) and path.suffix==".dsu":
        return ifO(flist)



def ifC(p:list,path):
    'create a file with wanted name'
    na=p[3]+".dsu"
    path=pa(p)
    path=path.joinpath(na)
    f=open(path,"x")
    print("Create your profile Information\n")
    dsuserver=input("server: ")
    username=input("username: ")
    password=input("password: ")
    profile=Profile.Profile(dsuserver=dsuserver,username=username,password=password)
    profile.save_profile(path)
    print("infomation added")
    f.close()


def ifR(p:list)->list:
    'read contend of the determined file'
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
def have_para_by_file():
    print("R [path]   for readlines")
    print("C [path} -n [filename]    for create new file and saving the profile")
    print("O [path] for loading the profile")
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
    print("do you want to create/check/load your profile? Yes or No")
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
