import pymongo
if __name__=="__main__":
        client=pymongo.MongoClient("mongodb://localhost:27017")
        print("MngoClient",client)
        db=client['Yazib']
        collection = db["MySampleCollection"]

        rec={'name':"Yazib"}
        # collection.delete_one(rec)
        # up=collection.update_many(prev,next1)   hello everyone
        delMany=collection.delete_many(rec)
        print(delMany.deleted_count)

        