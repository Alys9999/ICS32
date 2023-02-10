import json
import tool

'reverse geocoding by nomi file'
def rfile(path:str)->list:
    database=path
    with open(database,"rb") as f:
        dict1=json.load(f)
        rfile=[dict1['display_name']]
        return rfile


'get center json file from file'
def cfilelist(path:str)->list:
    database=path
    with open(database,"rb") as f:
        data=json.load(f)
        dict1=data[0]
        cfilelist=[dict1['lat'],dict1['lon']]
        return cfilelist



'''get purpleair json file from file'''
def pfilelist(path:str)->list:
    database=path
    with open(database,"rb") as f:
        data=json.load(f)
        filelist=data["data"]
    return filelist

'''exclude not answering sensor'''
def answeredlist(filelist:list)->list:
    answeredlist=list()
    for x in range(len(filelist)-1):
        y=data2[x]
        if y[4]<3600:
            answeredlist.append(y)
    return answeredlist

'''exclude indoor sensors'''
def outdoorlist(answeredlist:list)->list:
    outdoorlist=list()
    for x in range(len(answeredlist)-1):
        y=answeredlist[x]
        if y[25]!=0:
            outdoorlist.append(y)
    return outdoorlist

'''take 28,29 para from outdoorlist(good list)
and exlude the geo out of distance from center'''
def inrangelist(outdoorlist:list,center:list,distance:int)->list:
    inrangeList=list()
    for x in range(len(outdoorlist)-1):
        y=outdoorlist[x]
        if tool.geoToDis(y[27],y[28],center[0],center[1])<distance:
            inrangeList.append(y)
    return inrangeList
        

'''the list more than AQI start'''
def threList(inrangelist:list,threshold:int)->list:
    threlist=list()
    for x in range(len(inrangelist)-1):
        y=inrangelist[x]
        aqi=tool.pToA(y[1])
        raqi=round(aqi)
        if aqi>=threshold:
            threlist.append(y)
            return threlist

'sort threlist by pm '
def pmsort(threlist:list)->list:
    for i in range(len(threlist)-1):
        for j in range(len(threlist)-i-1):
            if threlist[j][1]<threlist[j+1][1]:
                threlist[j],threlist[j+1]=threlist[j+1],threlist[j]
    return threlist
    
    
'limit by max'
def limitmax(threlist:list,maxnum:int)->list:
    return threlist[0:maxnum]
    
    

    
    
    
    
    
    
