import pymongo
if __name__=="__main__":
        client=pymongo.MongoClient("mongodb://localhost:27017")
        print("MngoClient",client)
        a=client.list_database_names()
        print(a)
        allDatabsesCol=client['Yazib']
        print(allDatabsesCol.list_collection_names())