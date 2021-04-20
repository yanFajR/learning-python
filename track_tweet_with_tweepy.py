from __future__ import print_function
import tweepy   
import json    
import datetime  
keywords = input("keywords: ")
f = open("Hasil.txt", "w")
CONSUMER_KEY = input("CONSUMER_KEY: ")        
CONSUMER_SECRET = input("CONSUMER_SECRET: ")
ACCESS_TOKEN = input("ACCESS_TOKEN: ") 
ACCESS_TOKEN_SECRET = input("ACCESS_TOKEN_SECRET: ") 
class StreamListener(tweepy.StreamListener):    
        def on_connect(self):           
                print("You are now connected to the streaming API.")
        def on_error(self, status_code):  
                print("An Error has occured: " + repr(status_code))
                return False
        def on_data(self, data):   
                try:    
                        datajson = json.loads(data)  
                        username = datajson["user"]["screen_name"]
                        cuitan = datajson["text"].lower()               
                        tweet = [{"User Name":username, "Tweet":cuitan}]
                        tulis = str(tweet)+"\n"
                        f.write(tulis)
                except Exception as e:
                        print(e)
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)   #autentikasi ke api twitter deengan konsumer key dan consumer secret
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)        #set acces token
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))  #gunakan listener tweet
streamer = tweepy.Stream(auth=auth, listener=listener)  #gunakan streamer
streamer.filter(track=keywords)
