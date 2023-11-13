from flask import Flask
from flask_pymongo import PyMongo
app=Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDataBase"
db=PyMongo(app).db

@app.route('/insert')
def Insert():
    db.inventory.insert_many([{'name':'yazib'},{'name':"Yazib","marks":45},{'name':"Yazib","marks":45}])
    return 'Insert successfully'


@app.route('/find')
def Find():
    find_1=db.inventory.find_one()
    print(find_1)
    return 

app.run(debug=True)