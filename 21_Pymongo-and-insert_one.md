#### 21. Pymongo and insert_one

![](images/21/1.png)

###### `using_insert_one.py`

```python
#!/usr/bin/env python
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")


def insert_two():

    # get a handle to the school database
    db = connection.school
    people = db.people

    print "insert, reporting for duty"

    richard = {"name": "Richard Kreuter", "company": "MongoDB",
               "interests": ['horses', 'skydiving', 'fencing']}
    andrew = {"_id": "erlichson", "name": "Andrew Erlichson",
              "company": "MongoDB", "interests": ['running', 'cycling',
                                                  'photography']}

    try:
        people.insert_one(richard)
        people.insert_one(andrew)

    except Exception as e:
        print "Unexpected error:", type(e), e

    print(richard)
    print(andrew)


if __name__ == '__main__':
    insert_two()
```

```sh
u64@vm:~/Desktop$ python using_insert_one.py
insert, reporting for duty
{'interests': ['horses', 'skydiving', 'fencing'], 'company': 'MongoDB', '_id': ObjectId('5abeda2e686c82213a952a2e'), 'name': 'Richard Kreuter'}
{'interests': ['running', 'cycling', 'photography'], 'company': 'MongoDB', '_id': 'erlichson', 'name': 'Andrew Erlichson'}
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
> use school
switched to db school
> show collections
people
scores
> db.people.find().pretty()
{
	"_id" : ObjectId("5abeda2e686c82213a952a2e"),
	"interests" : [
		"horses",
		"skydiving",
		"fencing"
	],
	"company" : "MongoDB",
	"name" : "Richard Kreuter"
}
{
	"_id" : "erlichson",
	"interests" : [
		"running",
		"cycling",
		"photography"
	],
	"company" : "MongoDB",
	"name" : "Andrew Erlichson"
}
>
bye
u64@vm:~/Desktop$
```