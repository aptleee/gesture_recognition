import numpy as np
from sklearn.svm import SVC
from pymongo import MongoClient
import pickle
t = []
l = []
client = MongoClient()
db = client.cool_database
collection = db.go
posts = db.posts
for post in posts.find({"label" : 1}): 
     t.append(post['data'])
for post in posts.find({"label" : 2}): 
     t.append(post['data'])
for post in posts.find({"label" : 3}): 
     t.append(post['data'])
for post in posts.find({"label" : 4}):
    t.append(post['data'])
for post in posts.find({"label" : 5}):
    t.append(post['data'])
for post in posts.find({"label" : 6}):
    t.append(post['data'])
for post in posts.find({"label" : 7}):
    t.append(post['data'])
for post in posts.find({"label" : 8}):
    t.append(post['data'])
l = 118*[1] + 101*[2] + 100*[3] + 100*[4] + 103*[5] + 100*[6] + 100*[7] + 100*[8]
X = np.asarray(t)    
y = np.array(l)
clf = SVC(gamma='auto',decision_function_shape='ovo', kernel = 'linear')
clf.fit(X, y)
with open('clf.pickle', 'wb') as f:
        pickle.dump(clf, f)
