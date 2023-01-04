import requests
import json

def conv2url(appid,about,**params):
    param="".join([f"&{i}={params[i]}" for i in params])
    if about.count("/")==1:
      return f"https://api.worldofwarships.asia/wows/{about}/?application_id={appid}{param}"
  
def get_json(appid,about,**params) -> dict:
    data=json.loads(requests.get(conv2url(appid,about,**params)).content)
    return data
