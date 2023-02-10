from urllib import request,error
import urllib, json
'''
Application name  ICS 32 Assignment 3
API key           35454afb241a95f38f45d2d1b8f4c531
Shared secret     590b77fc9cc490067bbb71d5a34f67f7
Registered to     Alyys999
'''
class LastFM:
    
    def __init__(self,artist="Cher",album="Believe"):
        self.url=""
        self.artist=artist
        self.album=album
        self.listeners=0
        self.playcount=0
        self.summary=""
        self.tracks=""
        self.tags=""

    
    def set_apikey(self, apikey:str) -> None:
        
        artist=self.artist
        album=self.album
        self.url = f"https://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={apikey}&artist={artist}&album={album}&format=json"

        
    def _download_url(self,url_to_download: str) -> dict:
        try:
            response = urllib.request.urlopen(url_to_download)
            json_results = response.read()
            data = json.loads(json_results)
            
        except urllib.error.HTTPError as e:
            print('Failed to download contents of URL')
            print('Status code: {}'.format(e.code))
        finally:
            if response != None:
                response.close()
        return data


    def load_data(self) -> None:
        song_names=[]
        tag=[]
        rdata=self._download_url(self.url)

        self.listeners=rdata["album"]["listeners"]
        self.playcount=rdata["album"]["playcount"]
        self.summary=rdata["album"]["wiki"]["summary"]
        tracks=rdata["album"]["tracks"]["track"]
        for x in tracks:
            song_names.append(x["name"])
        self.song_name=song_names
        tags=rdata["album"]["tags"]["tag"]
        for i in tags:
            tag.append(i["name"])
        self.tags=tag
        
                
    def transclude(self, message:str) -> str:
        a=message.replace("@lastfm",self.summary)
        return a
                