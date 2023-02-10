from urllib import request,error
from urllib import parse as p
import urllib, json
from abc import ABC
from abc import abstractmethod

class AuthorizationError(Exception):
    pass

class parameterError(Exception):
    pass

class invalidCountryName(BaseException):
    pass


class WebAPI:
    """handling http error here"""
    def _download_url(self,url: str) -> dict:
        try:
            response = urllib.request.urlopen(url)
            json_results = response.read()
            data = json.loads(json_results)
            
        except urllib.error.HTTPError as e:
            if e.code==401:
                raise AuthorizationError()
            elif e.code==404:
                raise parameterError()
        finally:
            try:
                if response != None:
                    response.close()
            except UnboundLocalError:
                pass
        return data


    def set_apikey(self, apikey:str=None) -> None:
        self.apikey=apikey

        """
        if self.url_type=="OpenWeather":
            zipcode=self.zipcode
            ccode=self.ccode
            self.url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{ccode}&appid={apikey}"
        elif self.url_type=="LastFM":
            artist=self.artist
            album=self.album
            self.url = f"https://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={apikey}&artist={artist}&album={album}&format=json"
        elif self.url_type=="ExtraCreditAPI":
            tup1=tuple([("q",self.name)])
            tup2=p.urlencode(tup1)
            self.url=(f"https://nominatim.openstreetmap.org/search?{tup2}&format=json")
            """
    @abstractmethod
    def load_data(self):
        pass
    
    @abstractmethod
    def transclude(self, message:str) -> str:
        pass
