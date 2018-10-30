import numpy as np
from sklearn.svm import SVC
from pymongo import MongoClient
l = []
client = MongoClient()
db = client.training_database
collection = db.traning_collection
X = np.asarray()
posts = db.posts
for post in posts.find(): 
     t.append(post['data']) 
X = np.asarray(t)    
y = np.array([])
clf = SVC(gamma='auto')
clf.fit(X, y)
clf.predict([[]])
