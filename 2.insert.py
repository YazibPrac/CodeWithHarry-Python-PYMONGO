import pymongo
if __name__=="__main__":
        client=pymongo.MongoClient("mongodb://localhost:27017")
        print("MngoClient",client)
        db=client['Yazib']
        collection = db["MySampleCollection"]
        # dictionary = {'name':"Yazib","marks":45}
        # collection.insert_one(dictionary)
        # dictionary1 = {'name':"Yazib1","marks":45}
        # collection.insert_one(dictionary1)
        insertThese=[
            {'_id':1,'name':"Yazib 9857","marks":45},
            {'_id':2,'name':"Ameen 12","marks":45},
            {'_id':2,'name':"noman 18","marks":45},
            ]
        collection.insert_many(insertThese)