import os.path as o
import os
from pathlib import Path
import pathlib
import shutil
import time



'''transform list to path'''
def ltp(oal):
    for x in oal:
        print (x)
    
'''print and return files in the dirctory'''
def ifD(p):
    od=[]
    of=[]
    for x in p.iterdir():
            
        if x.is_dir():
            od.append(x)
            od.sort()
        else:
            of.append(x)
            of.sort()
    od.extend(of)
    ltp(od)
    return od

'''print and return files in dir and subdir'''
def ifR(p):
    od=[]
    of=[]
    for x in p.iterdir():
        if x.is_dir():
            od.append(x)
            od.sort()
            ifR(x)
        else:
            of.append(x)
            of.sort()
    od.extend(of)
    ltp(od)
    return od

'''get the input and decide what to do'''

def input1():
    
    '''Seperate input'''
    first=input("this is input:")
    path1=first[2:]
    path2=pathlib.PurePath(path1)
    comm=first[0:2]


    '''if it is exist and is a directory'''

    if (not o.exists(path2))or(not Path.is_dir(path2)):
        print("ERROR")
        input1()
    else:
        if comm=="R ":
             return ifR(path2)
        elif comm=="D ":
            return ifD(path2)
        else:
            print("ERROR")
            input1()

    
'''return all'''
def ifA(lfi2):
    ltp(lfi2)
    return lfi2
    
'''return wanted names'''
def ifN(name,lfi2):
    forN=[]
    for x in lfi2:
        if o.basename(x) == name:
            forN.append(x)
    ltp(forN)
    return forN

'''return wanted .* files'''
def ifE(ex,lfi2):
    forE=[]
    for x in lfi2:
        p=Path(x)
        if p.suffix==ex:
            forE.append(x)
    ltp(forE)
    return forE

'''return files with wanted text'''
def ifTT(tex,lfi2):
    forTT=[]
    for x in lfi2:
        try:
            open(x,"r")
            if tex in open(x,"r"):
                forTT.append(x)
        except:
            pass
        continue
    ltp(forTT)
    return forTT

'''return files smaller than wanted bytes number'''
def ifSma(num,lfi2):
    forSma=[]
    for x in lfi2:
        try:
            xb=x.read_bytes()
            xbl=len(xb)
            if xbl<int(num):
                forSma.append(x)
        except IOError:
            pass
        continue
    ltp(forSma)
    return forSma

'''return files bigger than wanted bytes number'''
def ifLar(numL,lfi2):
    forLar=[]
    for x in lfi2:
        try:
            xb=x.read_bytes()
            xbl=len(xb)
            if xbl<int(numL):
                forLar.append(x)
        except:
            pass
        continue
    ltp(forLar)
    return forLar

'''get the input and decide what to do'''
def input2(last):
    first=input("this is input:")
    path1=first[2:]
    comm=first[0:2]
    if comm=="A":
        return ifA(last)
    elif comm=="N ":
        return ifN(path1,last)
    elif comm=="E ":
        return ifE(path1,last)
    elif comm=="T ":
        return ifTT(path1,last)
    elif comm=="< ":
        return ifSma(path1,last)
    elif comm=="> ":
        return ifLar(path1,last)
    else:
        print("ERROR")
        input2(last)

'''return files can be opened by txt'''
def ifF(lfi3):
    for x in lfi3:
        if x.suffix==".txt":
            fo=open(x)
            line=fo.readline()
            print(line)
        elif x.suffix!=".txt":
            print("NOT TEXT")

'''copy files with .dup extension'''
def ifDDD(lfi3):
    for x in lfi3:
        xs=str(x)
        xd=xs+".dup"
        xp=Path(xd)
        try:
            shutil.copy(x,xp)
        except IOError:
            pass
        continue

'''touch files'''
def ifTTT(lfi3):
    for x in lfi3:
        os.utime(x)


'''get input and what to do'''
def input3(last2):
    first=input("this is input:")
    comm=first[0:2]
    if comm[0]=="F":
        return ifF(last2)
    elif comm[0]=="D":
        return ifDDD(last2)
    elif comm[0]=="T":
        return ifTTT(last2)
    else:
        print("ERROR")
        input3(last2)

'''start from input1 and do the whole process'''
def aL():
    a=input1()
    b=input2(a)
    input3(b)


if __name__=="__main__":
    aL()