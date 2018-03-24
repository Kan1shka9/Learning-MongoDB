#### 5. Pymongo Exception

```sh
u64@vm:~$ sudo service mongod start
[sudo] password for u64: 
u64@vm:~$ 
```

###### Causing the exception

`pymongo_exception.py `

```python
#!/usr/bin/env python
import pymongo

# Do not need to import sys

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.test
users = db.users

doc = {'firstname':'Kanishka', 'lastname':'sunnam'}
print doc
print "about to insert the document"

try:
    users.insert_one(doc)
except Exception as e:
    print "insert failed:", e

print doc
print "inserting again"

try:
    users.insert_one(doc)
except Exception as e:
    print "second insert failed:", e

print doc

```

```sh
u64@vm:~/Desktop$ python pymongo_exception.py 
{'lastname': 'sunnam', 'firstname': 'Kanishka'}
about to insert the document
{'lastname': 'sunnam', '_id': ObjectId('5ab69b4f686c8219a86f67fe'), 'firstname': 'Kanishka'}
inserting again
second insert failed: E11000 duplicate key error collection: test.users index: _id_ dup key: { : ObjectId('5ab69b4f686c8219a86f67fe') }
{'lastname': 'sunnam', '_id': ObjectId('5ab69b4f686c8219a86f67fe'), 'firstname': 'Kanishka'}
u64@vm:~/Desktop$ 
```

```sh
u64@vm:~$ mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
Server has startup warnings: 
2018-03-24T11:39:08.382-0700 I STORAGE  [initandlisten] 
2018-03-24T11:39:08.382-0700 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2018-03-24T11:39:08.382-0700 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2018-03-24T11:39:09.562-0700 I CONTROL  [initandlisten] 
2018-03-24T11:39:09.562-0700 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2018-03-24T11:39:09.562-0700 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2018-03-24T11:39:09.562-0700 I CONTROL  [initandlisten] 
> db.users.find()
{ "_id" : ObjectId("5ab69b4f686c8219a86f67fe"), "lastname" : "sunnam", "firstname" : "Kanishka" }
> db.users.find().pretty()
{
	"_id" : ObjectId("5ab69b4f686c8219a86f67fe"),
	"lastname" : "sunnam",
	"firstname" : "Kanishka"
}
> 
```

###### Fixing the program

```sh
> db.users.drop()
true
> 
```

`pymongo_exception-fix.py`

```python
#!/usr/bin/env python
import pymongo

# Do not need to import sys

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.test
users = db.users

doc = {'firstname':'Kanishka', 'lastname':'sunnam'}
print doc
print "about to insert the document"

try:
    users.insert_one(doc)
except Exception as e:
    print "insert failed:", e

print doc
print "inserting again"
doc = {'firstname':'Kanishka', 'lastname':'sunnam'}

try:
    users.insert_one(doc)
except Exception as e:
    print "second insert failed:", e

print doc
```

```sh
u64@vm:~/Desktop$ python pymongo_exception-fix.py 
{'lastname': 'sunnam', 'firstname': 'Kanishka'}
about to insert the document
{'lastname': 'sunnam', '_id': ObjectId('5ab69cc7686c821a07a1ef28'), 'firstname': 'Kanishka'}
inserting again
{'lastname': 'sunnam', '_id': ObjectId('5ab69cc7686c821a07a1ef29'), 'firstname': 'Kanishka'}
u64@vm:~/Desktop$
```

```sh
> db.users.find()
{ "_id" : ObjectId("5ab69cc7686c821a07a1ef28"), "lastname" : "sunnam", "firstname" : "Kanishka" }
{ "_id" : ObjectId("5ab69cc7686c821a07a1ef29"), "lastname" : "sunnam", "firstname" : "Kanishka" }
> db.users.find().pretty()
{
	"_id" : ObjectId("5ab69cc7686c821a07a1ef28"),
	"lastname" : "sunnam",
	"firstname" : "Kanishka"
}
{
	"_id" : ObjectId("5ab69cc7686c821a07a1ef29"),
	"lastname" : "sunnam",
	"firstname" : "Kanishka"
}
> 
```