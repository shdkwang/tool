from pymongo import MongoClient
import pymongo
import json
from datetime import datetime
import sys
import os

DB_NAME = 'pathdump'
COLL_NAME = 'TIB'
client = MongoClient('localhost', 27017)
database = client[DB_NAME]
collection = database[COLL_NAME]

hostname = sys.argv[1]
cmd="mongoimport --db " + DB_NAME + " --collection " + COLL_NAME + " <"+hostname+"_new.json"
print cmd
os.system(cmd)
collection.create_index([("path",pymongo.ASCENDING),("log",pymongo.ASCENDING),("dport",pymongo.ASCENDING),("id",pymongo.ASCENDING),("bytes",pymongo.ASCENDING)])
