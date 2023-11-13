import pymongo
if __name__=="__main__":
        client=pymongo.MongoClient("mongodb://localhost:27017")
        print("MngoClient",client)
        db=client['Yazib']
        collection = db["MySampleCollection"]

        prev={'name':"Yazib"}
        next1={'$set':{'marks':79}}
        collection.update_one(prev,next1)
        up=collection.update_many(prev,next1)
        print(up.modified_count)