from urllib import request,error
import urllib, json
from WebAPI import WebAPI

"""a842eb8cce6a0e06ec2c8d8ac5ae2518"""

class OpenWeather(WebAPI):
    
    def __init__(self,zipcode="92697",ccode="US"):
        self.apikey=""
        self.url=""
        self.data=""
        self.zipcode=zipcode
        self.ccode=ccode
        self.temperature=0.00
        self.high_temperature=0.00
        self.low_temperature=0.00
        self.longitude=0.00
        self.latitude=0.00
        self.description=None
        self.humidity=0
        self.sunset=0
        self.city=None
        

    def load_data(self) -> None:
        zipcode=self.zipcode
        ccode=self.ccode
        apikey=self.apikey
        self.url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{ccode}&appid={apikey}"

        rdata=self._download_url(self.url)
        self.temperature=rdata["main"]["temp"]
        self.high_temperature=rdata["main"]["temp_max"]
        self.low_temperature=rdata["main"]["temp_min"]
        self.longitude=rdata["coord"]["lon"]
        self.latitude=rdata["coord"]["lat"]
        self.description=rdata["weather"][0]["description"]
        self.humidity=rdata["main"]["humidity"]
        self.sunset=rdata["sys"]["sunset"]
        self.city=rdata["name"]

                
    def transclude(self, message:str) -> str:
        a=message.replace("@weather",self.description)
        return a
                

