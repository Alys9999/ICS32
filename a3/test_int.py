from LastFM import LastFM
from OpenWeather import OpenWeather
from ExtraCreditAPI import ExtraCreditAPI as ex
from WebAPI import WebAPI

def test_api(message:str, apikey:str, webapi:WebAPI):
    webapi.set_apikey(apikey)
    webapi.load_data()
    result = webapi.transclude(message)
    print(result)


open_weather = OpenWeather("99999999") #notice there are no params here...HINT: be sure to use parameter defaults!!!
test_api("Testing the weather: @weather", "a842eb8cce6a0e06ec2c8d8ac5ae2518", open_weather)
# expected output should include the original message transcluded with the default weather value for the @weather keyword.



'''lastfm = LastFM()
test_api("Testing lastFM: @lastfm", "35454afb241a95f38f45d2d1b8f4c531", lastfm)
# expected output include the original message transcluded with the default music data assigned to the @lastfm keyword


extra=ex()
test_api("Testing the ex: @extracredit",None,extra)

'''










'''
artist="Cher"
album="Believe"
apikey = "35454afb241a95f38f45d2d1b8f4c531"

zipcode = "92697"
ccode = "US"
apikey2 = "a842eb8cce6a0e06ec2c8d8ac5ae2518"

lastFM = LastFM(artist,album)
url=lastFM.set_apikey(apikey)
lastFM.load_data()
a=lastFM.transclude("this is the summary @lastfm")
print(a)

open_weather = OpenWeather(zipcode, ccode)
url2=open_weather.set_apikey(apikey2)
data2=open_weather._download_url(url2)
open_weather.load_data(data2)

a=open_weather.transclude("this is the weather today @weather")
print(a)
print(f"The temperature for {zipcode} is {open_weather.temperature} degrees")



print(lastFM.listeners)
print(lastFM.playcount)
print(lastFM.summary)
print(lastFM.tracks)
print(lastFM.tags)
print(lastFM.song_name)
'''