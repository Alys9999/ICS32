from urllib import request,error
import urllib, json

"""a842eb8cce6a0e06ec2c8d8ac5ae2518"""

class OpenWeather:
    
    def __init__(self,zipcode="92697",ccode="US"):
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
    
    def set_apikey(self, apikey:str) -> None:
        
        zipcode=self.zipcode
        ccode=self.ccode
        url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{ccode}&appid={apikey}"
        self.url=url
       
    def _download_url(self) -> dict:
        try:
            response = urllib.request.urlopen(url_to_download)
            json_results = response.read()
            data = json.loads(json_results)
            self.data=data
        except urllib.error.HTTPError as e:
            print('Failed to download contents of URL')
            print('Status code: {}'.format(e.code))
        finally:
            if response != None:
                response.close()


    def load_data(self) -> None:
        rdata=self.data
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
                
