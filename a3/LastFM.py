from urllib import request,error
import urllib, json
from WebAPI import WebAPI
import WebAPI as waClass
'''
Application name  ICS 32 Assignment 3
API key           35454afb241a95f38f45d2d1b8f4c531
Shared secret     590b77fc9cc490067bbb71d5a34f67f7
Registered to     Alyys999
'''


class LastFM(WebAPI):
    """having an instance"""
    def __init__(self,country="spain",limit="1"):
        self.apikey=""
        self.url=""
        self.data=""
        self.country=country
        self.limit=limit
        self.top_artists=[]


    def load_data(self) -> None:
        """load the data"""
        artists=[]
        limit=self.limit
        country=self.country
        apikey=self.apikey
        self.url = f"http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country={country}&limit={limit}&api_key=35454afb241a95f38f45d2d1b8f4c531&format=json"
      
        rdata=self._download_url(self.url)
        if rdata.get("error")!=None:
            if rdata["error"]==6:
                raise waClass.invalidCountryName
        else:
            for x in rdata["topartists"]["artist"]:
                artist=x["name"]
                artists.append(artist)
            artists=str(artists)
            self.top_artists=artists

        
                
    def transclude(self, message:str) -> str:
        """make the transclusion"""
        a=message.replace("@lastfm",self.top_artists)
        return a
                
