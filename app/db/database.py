from pymongo import MongoClient

client = MongoClient(host='mongodb://docker:mongopw@localhost', port=55001)
db = client["todo"]
msg_collection = db["task"]






async def add_task(payload):
    msg_collection.insert_one(payload)


async def delete_task(payload):
    msg_collection.delete_one(payload)
