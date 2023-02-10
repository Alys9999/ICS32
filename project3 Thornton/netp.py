import urllib.request as u
import urllib.parse as p
import json


'get purpleair in list online'
def ppa()->list:
    ppa=u.Request("https://www.purpleair.com/data.json", method="GET")
    ppa=u.urlopen(ppa)
    ppa=json.load(ppa)
    ppa=ppa['data']
    return ppa


'get center by spot name through NOMINATIM'
def nomigetc(name:str)->list:
    tup1=tuple([("q",name)])
    tup2=p.urlencode(tup1)
    url=(f"https://nominatim.openstreetmap.org/search?{tup2}&format=json")
    nomi=u.Request(url)
    nomi=u.urlopen(nomi)
    nomi=json.load(nomi)
    nomi=nomi[0]
    centerlist=[nomi['lat'],nomi['lon']]
    return centerlist




'get spot name by center through NOMI'
def nomigetn(center:list)->str:
    lat=center[0]
    lon=center[1]
    url=(f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json&accept-language=english")
    nomi=u.Request(url)
    nomi=u.urlopen(nomi)
    nomi=json.load(nomi)
    spot=nomi['display_name']
    return spot


    
    
    
    
    
    
    
    
    