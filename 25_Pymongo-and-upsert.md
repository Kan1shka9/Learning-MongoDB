#### 25. Pymongo and upsert

![](images/25/1.png)

###### `using_upsert.py`

```python
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")
db = connection.test
things = db.things

def using_upsert():

    print "updating with upsert"

    try:

        # lets remove all stuff from things
        things.drop()

        things.update_one({'thing':'apple'}, {'$set':{'color':'red'}}, upsert=True)
	things.update_many({'thing':'banana'}, {'$set':{'color':'yellow'}}, upsert=True)
        things.replace_one({'thing':'pear'}, {'color':'green'}, upsert=True)


        apple = things.find_one({'thing':'apple'})
        print "apple: ", apple
        banana = things.find_one({'thing':'banana'})
        print "banana: ", banana 
        pear = things.find_one({'thing':'pear'})
        print "pear: ", pear

    except Exception as e:
        print "Unexpected error:", type(e), e
        raise


using_upsert()
```

```sh
u64@vm:~/Desktop$ python using_upsert.py
updating with upsert
apple:  {u'color': u'red', u'thing': u'apple', u'_id': ObjectId('5abee9ad09c41a95745d8e2d')}
banana:  {u'color': u'yellow', u'thing': u'banana', u'_id': ObjectId('5abee9ad09c41a95745d8e2f')}
pear:  None
u64@vm:~/Desktop$
```

```sh
u64@vm:~/Desktop$ mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
Server has startup warnings:
2018-03-30T09:49:35.659-0700 I STORAGE  [initandlisten]
2018-03-30T09:49:35.659-0700 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2018-03-30T09:49:35.659-0700 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2018-03-30T09:49:36.582-0700 I CONTROL  [initandlisten]
2018-03-30T09:49:36.582-0700 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2018-03-30T09:49:36.582-0700 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2018-03-30T09:49:36.583-0700 I CONTROL  [initandlisten]
> show dbs
admin   0.000GB
config  0.000GB
reddit  0.000GB
school  0.000GB
test    0.000GB
> use test
switched to db test
> show collections
things
> db.things.find()
{ "_id" : ObjectId("5abee9ad09c41a95745d8e2d"), "thing" : "apple", "color" : "red" }
{ "_id" : ObjectId("5abee9ad09c41a95745d8e2f"), "thing" : "banana", "color" : "yellow" }
{ "_id" : ObjectId("5abee9ad09c41a95745d8e31"), "color" : "green" }
>
bye
u64@vm:~/Desktop$
```