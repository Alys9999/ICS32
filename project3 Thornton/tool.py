import math as m


'''convert two geopoints to distance'''
def geoToDis(lat1,lon1,lat2,lon2):
    lat1=m.fabs(lat1)
    lon1=m.fabs(lon1)
    lat2=m.fabs(lat2)
    lon2=m.fabs(lon2)
    lon1, lat1, lon2, lat2 = map(m.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = m.sin(dlat/2)**2 + m.cos(lat1) * m.cos(lat2) * m.sin(dlon/2)**2
    c = 2 * m.asin(m.sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r
    
'''calculating AQI with pm'''
def pToA(pm:float)->float:
    if pm>=0.0 and pm<12.1:
        AQI=(pm/12.0)*50
        return AQI
    elif pm>=12.1 and pm<35.5:
        AQI=50+((pm-12.1)/(35.4-12.1))*(101-50)
        return AQI
    elif pm>=35.5 and pm<55.5:
        AQI=100+((pm-35.5)/(55.4-35.5))*(151-100)
        return AQI
    elif pm>=55.5 and pm<150.5:
        AQI=150+((pm-55.5)/(150.4-55.5))*(201-150)
        return AQI
    elif pm>=150.5 and pm<250.5:
        AQI=200+((pm-150.5)/(250.4-150.5))*(301-200)
        return AQI
    elif pm>=250.5 and pm<350.5:
        AQI=300+((pm-250.5)/(350.4-250.5))*(401-300)
        return AQI
    elif pm>=350.5 and pm<500.5:
        AQI=400+((pm-350.5)/(500.4-350.5))*(501-400)
        return AQI
    else:
        AQI=501
        return AQI

'''take valid input'''
def inputOne()->list:
    a=input()
    a=a.replace('CENTER ','')
    for x in range(len(a)):
        if a[x]==' ':
            sign=a[:x]
            name=a[x+1:]
            break
    blist=[sign,name]
    return blist

    
'''second input'''
def rang():
    a=input()
    a=a.replace("RANGE ",'')
    a=int(a)
    return a

    
'''third input'''
def threshold():
    a=input()
    a=a.replace("THRESHOLD ",'')
    a=int(a)
    return a

    
'''Fourth input'''
def maxnum():
    a=input()
    a=a.replace("MAX",'')
    a=int(a)
    return a

    
'''Fifth input'''
def inputFive():
    a=input()
    a=a.replace("AQI ",'')
    if a[0]=="P":
        signp='PURPLEAIR'
        return signp
    elif a[0]=='F':
        for x in range(len(a)-1):
            if a[x]==' ':
                sign=a[:x]
                path=a[x+1:]
                break
        flist=[sign,path]
        return flist


    
'''Sixth input'''
def inputSix():
    a=input()
    a=a.replace("REVERSE ",'')
    if a[0]=="N":
        signn='NOMINATIM'
        return signn
    elif a[0]=='F':
        for x in range(len(a)-1):
            if a[x]==' ':
                sign=a[:x]
                path=a[x+1:]
                break
        flist=[sign,path]
        return flist
        

    
    