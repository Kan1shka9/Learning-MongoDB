#### 22. Pymongo and insert_many

###### `using_insert_many.py`

```python
#!/usr/bin/env python

import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")


def insert_many():
    # get a handle to the school database
    db = connection.school
    people = db.people

    print "insert_many, reporting for duty"
    andrew = {"_id": "erlichson", "name": "Andrew Erlichson",
              "company": "MongoDB",
              "interests": ['running', 'cycling', 'photography']}
    richard = {"name": "Richard Kreuter", "company": "MongoDB",
               "interests": ['horses', 'skydiving', 'fencing']}
    people_to_insert = [andrew, richard]
    try:
        people.insert_many(people_to_insert, ordered=False)
    except Exception as e:
        print "Unexpected error:", type(e), e


def print_people():
    # get a handle to the school database
    db = connection.school
    people = db.people
    cur = people.find({}, {'name': 1})
    for doc in cur:
        print doc

if __name__ == '__main__':
    print "Before the insert_many, here are the people"
    print_people()
    insert_many()
    print "\n\nAfter the insert_many, here are the people"
    print_people()
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
> use school
switched to db school
> show collections
people
scores
> db.people.drop()
true
>
bye
u64@vm:~/Desktop$
```

```sh
u64@vm:~/Desktop$ python using_insert_many.py
Before the insert_many, here are the people
insert_many, reporting for duty


After the insert_many, here are the people
{u'_id': u'erlichson', u'name': u'Andrew Erlichson'}
{u'_id': ObjectId('5abedcea686c8221c4a28b1c'), u'name': u'Richard Kreuter'}
u64@vm:~/Desktop$
```