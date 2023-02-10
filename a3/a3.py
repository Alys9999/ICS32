import pathlib as p
import Profile
import ds_client as dsc
import LastFM as lfm
from LastFM import LastFM
import OpenWeather as ow
from OpenWeather import OpenWeather
import ExtraCreditAPI as exclass
from ExtraCreditAPI import ExtraCreditAPI as ex
from WebAPI import WebAPI
import WebAPI as waClass

def process():
    """all"""
    while True:
        i=inputa()
        if i[0]in ("C","R","O"):
            a=decideCRO(i)
            if i[0]=="O" and a!=False:
                return a
            elif i[0]=="C" and a!=False:
                print("if you want to use any profile, load it with command O")
            else:
                print("invalid command, input again")
        else:
            print("invalid command, input again")
    
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
    i=True
    if flist[0]=="C" and validdir(path) and flist[2]=="-n":
        try:
            ifC(flist,path)
            return i
        except FileExistsError:
            print("file already exists")
    elif flist[0]=="R" and validfile(path) and path.suffix==".dsu":
        ifR(flist)
        return i
    elif flist[0]=="O" and validfile(path) and path.suffix==".dsu":
        return ifO(flist)
    else:
        return False



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
    """load the profile"""
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
    """indicate the correct way to manipulate the file system"""
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
            
def transcluded(message:str, apikey:str, webapi:WebAPI):
    """doing the transclusion"""
    webapi.set_apikey(apikey)
    webapi.load_data()
    result = webapi.transclude(message)
    return result


def pretrans():
    """accepting parameters and handeling error for pretrans"""
    message=input("message: ")
    if message.find("@weather") != -1:
        while True:
            try:
                zipcode=input("zipcode=")
                countryName=input("CountryName=")
                open_weather = OpenWeather(zipcode,countryName) #notice there are no params here...HINT: be sure to use parameter defaults!!!
                message=transcluded(message, "a842eb8cce6a0e06ec2c8d8ac5ae2518", open_weather)
                break
            except waClass.parameterError:
                print("invalid code or country name")
            
    if message.find("@lastfm") != -1:
        while True:
            try:
                max_num=input("the number of top artists you want: ")
                country=input("country=")
                lastfm = LastFM(country,max_num)
                message=transcluded(message, "35454afb241a95f38f45d2d1b8f4c531", lastfm)
                break
            except waClass.invalidCountryName:
                print("invalid country name")
                
    if message.find("@extracredit") !=-1:
        while True:
            try:
                name=input("addres is: ")
                extra=ex(name)
                message=transcluded(message,None,extra)
                break
            except waClass.parameterError:
                print("invalid address")
        
    return message
            


def valid_server():
    """take in a valid server"""
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
    """gives another choice when do not want to create a profile"""
    if com=="Yes":
        loaded_list=have_para_by_file()
        server=loaded_list[0]
        username=loaded_list[1]
        password=loaded_list[2]
    elif com=="No":
        server=input("server: ")
        username=input("username: ")
        password=input("password: ")
    ip=server
    port=2021
    """send the message"""
    while True:
        
        message=pretrans()
        print("Do you want to add bio? Yes or No")
        ifbio=valid_com()
        if ifbio=="Yes":
            bio=pretrans()
            r=dsc.send(ip,port,username,password,message,bio)
            if r!=None:
                print(r)
            profile=Profile.Profile(server,username,password)
            profile.bio=bio
        else:
            r=dsc.send(ip,port,username,password,message)
            if r!=None:
                print(r)
            profile=Profile.Profile(server,username,password)
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
