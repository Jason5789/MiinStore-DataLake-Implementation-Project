import random

from iottalkpy.dan import NoData
import pymongo
from pymongo import MongoClient
import datetime
import json
api_url = 'http://140.116.58.163:31480/csm'
client = MongoClient('mongodb://140.116.58.163:32001')
db = client.testdb
collection = db.test_collection

 
device_name = 'MongoDB'

 
device_model = 'MongoDB'

odf_list = ['Data-O']
 

def on_register(dan):
    print('register successfully')


def Data_O(data: list):
    print(str(data))
    time = datetime.datetime.utcnow()
    collection.insert_one({
    	"data": data,
    	"date": time
    })
