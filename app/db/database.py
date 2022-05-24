from pymongo import MongoClient

client = MongoClient(host='mongodb://docker:mongopw@localhost', port=55001)
db = client["todo"]
msg_collection = db["task"]

message = {
    "channel": "dev",
    "author": "cerami",
    "text": "Hello, world!"
}




async def add_task(payload):
    msg_collection.insert_one(payload)



#async def delete_task();
