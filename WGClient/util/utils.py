import requests
import json

def conv2url(appid,about,game="https://api.worldofwarships.asia/wows/",**params) -> str:
    param="".join([f"&{i}={params[i]}" for i in params])
    return f"{game}{about}/?application_id={appid}{param}"
  
def get_json(appid,about,**params) -> dict:
    data=json.loads(requests.get(conv2url(appid,about,**params)).content)
    return data