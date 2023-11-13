import pymongo
if __name__=="__main__":
        client=pymongo.MongoClient("mongodb://localhost:27017")
        print("MngoClient",client)
        db=client['Yazib']
        collection = db["MySampleCollection"]
        # one=collection.find_one({'name':'Yazib'},{'name':False})
        # print(one)

        allFind=collection.find({'name': 'Yazib','marks':{"$Lte":80}})
        # print(collection.count_documents())
        # print(allFind) hi every one
        for item in allFind:
            print(item)