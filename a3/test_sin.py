import urllib, json
from urllib import request,error
from urllib import parse as p
"""a842eb8cce6a0e06ec2c8d8ac5ae2518"""
def _download_url(url_to_download: str) -> dict:
    response = None
    r_obj = None

    try:
        response = urllib.request.urlopen(url_to_download)
        json_results = response.read()
        r_obj = json.loads(json_results)

    except urllib.error.HTTPError as e:
        print('Failed to download contents of URL')
        print('Status code: {}'.format(e.code))

    finally:
        if response != None:
            response.close()
    
    return r_obj

def main() -> None:
    name="Bren Hall,Irvine,CA"
    tup1=tuple([("q",name)])
    tup2=p.urlencode(tup1)
    url=(f"https://nominatim.openstreetmap.org/search?{tup2}&format=json")
    '''
    token_url = f"https://ws.audioscrobbler.com/2.0/?method=auth.gettoken&api_key={apikey}&format=json"
    token_obj = _download_url(token_url)
    token=token_obj["token"]
    print(token)
    auth_url=f"http://www.last.fm/api/auth/?api_key={apikey}&token={token}
    auth_obj=_download_url(auth_url)'
    print(auth_obj)
    '''
    info_obj=_download_url(url)
    if info_obj is not None:
        print(info_obj)


if __name__ == '__main__':
    main()