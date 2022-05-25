from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient(host='mongodb://docker:mongopw@localhost', port=55000)
db = client["todo"]
msg_collection = db["task"]


async def add_task(payload):
    msg_collection.insert_one(payload)



async def delete_task(payload):
    msg_collection.delete_one(payload)


async def get_show():
    for x in msg_collection.find({}, {'_id': False}).limit(10):
        print(x)
        return x


