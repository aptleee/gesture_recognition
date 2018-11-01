#!/usr/bin/env python
import tweepy
from socket import *
import json
import pickle
import numpy as np
from sklearn.svm import SVC
import requests
def weather():
    response = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyDtssI2pFiAwJZ7RnUlAvphbFmoHaWBoTo",data="geolocation-data")
    locationDict = response.json()
    location = locationDict["location"]
    accu = locationDict["accuracy"]
    latitute = location["lat"]
    lng = location["lng"]
    weatherURL = "http://api.openweathermap.org/data/2.5/weather?"
    APIkey = "e705bd48be7042195981bfe518892515"
    weatherURL += "lat=" + str(int(latitute)) + "&lon=" + str(int(lng)) + "&APPID=" + APIkey
    response = requests.post(weatherURL)
    Dict = response.json()
    tempInfo = Dict['weather'][0]
    temp = Dict['main']
    number = temp['temp']
    pressure = temp['pressure']
    desc = tempInfo['main']
    response.close()
    return (number, desc, pressure)


def tweets(tweet):
    # personal details 
    consumer_key ="nVgBPlIoglqdMdskfDeTLMvwF"
    consumer_secret ="FQVOiPKxsorF6ebWlJakX4Gnnlp9fLdwH2w6WacjbehqvvaxVB"
    access_token ="1047658775409319936-xOypj3u3f6dOZfMS9xNmT8qZv7CTSn"
    access_token_secret ="ez2G5Lz9uLIfafSDzKkidnKr7stB0qIUKrcpuK6TovhBC"
      
    # authentication of consumer key and secret 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    api = get_api(cfg)    
    # update the status 
    try:
        status = api.update_status(status = tweet)
    except tweepy.error.TweepError:
        pass
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 8085))
serverSocket.listen(1)
print('The server is ready to receive')
count = 0
l = []
while True:
    connectionSocket, addr = serverSocket.accept()
    data = connectionSocket.recv(2048)
    if data == '':
        connectionSocket.close()
    else:
        data1 = json.loads(data)
        if (isinstance(data1, list)):
            l = l + data1
            count += 1
            if count == 10:
                d = len(l)/2-25
                if d <= 0:
                    k = l
                else:
                    m = (len(l)/2 - 1)//d + 1
                    r = [x for c, x in enumerate(l) if c%(2*m)]
                    k = [x for c, x in enumerate(r) if c%(2*m-1)]
                    k = k[:50]
                if len(k) == 50:
                    with open('clf.pickle', 'rb') as f:
                        clf2 = pickle.load(f)
                        a = clf2.predict([k])
                        if a[0] == 1:
                            connectionSocket.send("c")
                        elif a[0] == 2:
                            connectionSocket.send("o")
                        elif a[0] == 3:
                            connectionSocket.send("l")
                        elif a[0] == 4:
                            connectionSocket.send("u")
                        elif a[0] == 5:
                            connectionSocket.send("m")
                        elif a[0] == 6:
                            connectionSocket.send("b")
                        elif a[0] == 7:
                            connectionSocket.send("i")
                        elif a[0] == 8:
                            connectionSocket.send("a")

                print(l)
                print(len(l))
                print(k)
                print(len(k))
                count = 0
                l = [] 
            connectionSocket.close()
        elif data1 == "weather":
            res = json.dumps(weather())
            connectionSocket.send(res)
            connectionSocket.close()
        elif data1.find("tweets") >= 0:
            tweet = data1[9:]
            tweets(tweet)
            connectionSocket.send(b'cool')
            connectionSocket.close()
# m =ii (l.length()-1)/d + 1
# from pymongo import MongoClint
# client = MongoClient()
# db = client.test_database

