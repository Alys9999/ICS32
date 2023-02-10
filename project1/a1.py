import pathlib as p




def process():
    'all'
    while True:
        i=inputa()
        if i[0]in ("Q","L","C","D","R"):
            a=decideQLCDR(i)
            if len(i)>2 and i[2]=="-r":
                b=decide_r(i,a)
                if len(i)>3 and (i[3] in ("-s", "-f", "-e")):
                    d=decide_sfe(i,b)
                    ltp(d)
                else:
                    ltp(b)
            elif len(i)>2 and (i[2] in ("-s","-f","-e")):
                c=decide_sfe(i,a)
                ltp(c)
            else:
                ltp(a)
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



def decideQLCDR(flist:list)->list:
    'take input and decide L Q C D R'
    if flist[0]=="Q":
        print("Closed")
        return ""
    elif flist[0]=="L":
        '''if it exist and is a directory'''
        path=pa(flist)
        if validdir(path):
            return ifL(path)
        else:
            retry()
    elif flist[0]=="C":
        path=pa(flist)
        if validdir(path) and flist[2]=="-n":
            return ifC(flist)
        else:
            retry()
    elif flist[0]=="D":
        path=pa(flist)
        if validfile(path):
            return ifD(flist)
        else:
            retry()
    elif flist[0]=="R":
        path=pa(flist)
        if validfile(path) and path.suffix==".dsu":
            return ifR(flist)
        else:
            retry()
    else:
        retry()

        

def decide_r(flist:list,lf:list):
    'make decision of r'
    repath=pa(flist)
    rf=ifr(repath)
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

        


def ifL(p)->list:
    'return files in the dirctory'
    od=[]
    of=[]
    for x in p.iterdir():
        if x.is_dir():
            od.append(x)
            od.sort()
        else:
            of.append(x)
            of.sort()
    of.extend(od)
    return of


def ifr(p):
    'return files in dir and subdir'
    od=[]
    of=[]
    for x in p.iterdir():
        if x.is_dir():
            od.append(x)
            od.sort()
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
    f.close()
    return path
    
def ifD(p:list)->list:
    'delete the determined file'
    path=pa(p)
    path.unlink()
    d=str(path)+" DELETED"
    return d

def ifR(p:list)->list:
    'read contend of the determined file'
    path=pa(p)
    a=path.open().read()
    if not a:
        print("EMPTY")
    else:
        p=a.strip()
        q=[p]
        return(q)
    a.close()
  
if __name__ == '__main__':
    
    process()
