from urllib import request,error
from urllib import parse as p
import urllib, json
from WebAPI import WebAPI
import WebAPI as waClass

class ExtraCreditAPI(WebAPI):
    
    def __init__(self,name="Bren Hall,Irvine,CA"):
        self.apikey=""
        self.name=name
        self.url=""
        self.data=""
        self.area=[]
        self.display_name=""
        self.place_type=""
        self.place_func=""
        

    def load_data(self) -> None:
        tup1=tuple([("q",self.name)])
        tup2=p.urlencode(tup1)
        apikey=self.apikey
        self.url=(f"https://nominatim.openstreetmap.org/search?{tup2}&format=json")
        rdata=self._download_url(self.url)
        if len(rdata)!=0:
            rdata=rdata[0]    
            self.area=rdata["boundingbox"]
            self.display_name=rdata["display_name"]
            self.place_type=rdata["class"]
            self.place_func=rdata["type"]
        else:
            raise waClass.parameterError

                
    def transclude(self, message:str) -> str:
        a=message.replace("@extracredit",self.display_name)
        return a