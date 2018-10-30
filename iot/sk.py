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
#for i in range(1,8):
   # l += 60 * [i]
l = 60 * [1] + 63 * [2] + 60 * [3]
X = np.asarray(t)    
y = np.array(l)
clf = SVC(gamma='auto',decision_function_shape='ovo')
clf.fit(X, y)
clf.predict([[]] 
clf.fit(X, y)
with open('save/clf.pickle', 'wb') as f:
        pickle.dump(clf, f)
clf.predict([[]]
with open('save/clf.pickle', 'rb') as f:
    clf2 = pickle.load(f)
print(clf2.predict(X[0:1]))
