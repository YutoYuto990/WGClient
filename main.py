from WGClient import Client
import os

api=os.getenv("wows_api")

client=Client(api,"ja")
user=client.wows.get_arena("エルメス")
print(user)



#https://api.worldoftanks.asia/wot/auth/login/?application_id=