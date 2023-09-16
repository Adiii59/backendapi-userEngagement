import os
from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv()

URI = os.environ.get("MONGODB_URI")
DB = os.environ.get("MONGODB_DATABASE")
COLLECTION = os.environ.get("MONGODB_COLLECTION")
client = MongoClient(URI, tls = True, tlsAllowInvalidCertificates = True)
db = client[DB]
collection = db[COLLECTION]


def createPlant(pid):
    collection.insert_one({"pid": pid, "Comments": []})

def getPlantComments(pid):
    x = collection.find({}, {"_id": 0, "pid": 1})
    pids = [_["pid"] for _ in x]
    if pid not in pids:
        createPlant(pid)
    x = collection.find({"pid": pid}, {"Comments": 1, "_id": 0})
    return [_["Comments"] for _ in x][0]

def addComment(pid, uid, comment = ""):
    collection.update_one(
    { "pid": pid },
    { "$addToSet": {"Comments": {"uid": uid, "comment": comment }}})
