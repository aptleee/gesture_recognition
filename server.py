from socket import *
import json
import datetime 
from pymongo import MongoClient
count = 0
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 8080))
serverSocket.listen(1)
print('The server is readty to receive')
l = []
client = MongoClient()
db = client.training_database
collection = db.traning_collection
posts = db.posts
while True:
    connectionSocket, addr = serverSocket.accept()
    data = connectionSocket.recv(2048)
    if data == '':
        connectionSocket.close()
    else:
        print(data)
        data1 = json.loads(data)
        l = l + data1
        connectionSocket.close()
        count += 1
        if count == 10:
            d = len(l)/2-50
            print("d", d)
            m = (len(l)/2 - 1)//d + 1
            print("m", m)
            r = [x for c, x in enumerate(l) if c%(2*m)]
            k = [x for c, x in enumerate(r) if c%(2*m-1)]
            k = k[:100]
	    post = {}
	    post["data"] = k
	    post["label"] = 2
	    post["name"] = "oooops"
	    post_id = posts.insert(post)
	    post_id = posts.insert(post)
	    print(post_id)
            print(l)
            print(len(l))
            print(k)
            print(len(k))
            count = 0
            l = []
# m =ii (l.length()-1)/d + 1
# from pymongo import MongoClint
# client = MongoClient()
# db = client.test_database

