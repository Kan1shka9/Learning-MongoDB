#### Homework 1.2

![](images/1.png)

```sh
u64@vm:~$ sudo service mongod start
[sudo] password for u64:
u64@vm:~$
```

```sh
u64@vm:~$ mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
Server has startup warnings: 
2018-03-24T12:27:20.225-0700 I STORAGE  [initandlisten] 
2018-03-24T12:27:20.225-0700 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2018-03-24T12:27:20.225-0700 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2018-03-24T12:27:23.406-0700 I CONTROL  [initandlisten] 
2018-03-24T12:27:23.406-0700 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2018-03-24T12:27:23.406-0700 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2018-03-24T12:27:23.406-0700 I CONTROL  [initandlisten] 
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
m101    0.000GB
> use m101
switched to db m101
> db
m101
> show collections
funnynumbers
hw1
> db.funnynumbers.find()
{ "_id" : ObjectId("50778ce69331a280cf4bcf7d"), "value" : 87 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf7e"), "value" : 34 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf7f"), "value" : 23 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf80"), "value" : 71 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf81"), "value" : 26 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf82"), "value" : 8 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf83"), "value" : 91 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf84"), "value" : 99 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf85"), "value" : 49 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf86"), "value" : 25 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf87"), "value" : 69 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf88"), "value" : 4 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf89"), "value" : 90 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf8a"), "value" : 39 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf8b"), "value" : 41 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf8c"), "value" : 17 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf8d"), "value" : 95 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf8e"), "value" : 14 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf8f"), "value" : 1 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf90"), "value" : 62 }
Type "it" for more
> it
{ "_id" : ObjectId("50778ce69331a280cf4bcf91"), "value" : 94 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf92"), "value" : 22 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf93"), "value" : 93 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf94"), "value" : 25 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf95"), "value" : 81 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf96"), "value" : 46 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf97"), "value" : 99 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf98"), "value" : 71 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf99"), "value" : 35 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf9a"), "value" : 19 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf9b"), "value" : 14 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf9c"), "value" : 89 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf9d"), "value" : 97 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf9e"), "value" : 90 }
{ "_id" : ObjectId("50778ce69331a280cf4bcf9f"), "value" : 52 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfa0"), "value" : 12 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfa1"), "value" : 91 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfa2"), "value" : 0 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfa3"), "value" : 67 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfa4"), "value" : 81 }
Type "it" for more
> it
{ "_id" : ObjectId("50778ce69331a280cf4bcfa5"), "value" : 53 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfa6"), "value" : 83 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfa7"), "value" : 85 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfa8"), "value" : 7 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfa9"), "value" : 15 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfaa"), "value" : 57 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfab"), "value" : 84 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfac"), "value" : 67 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfad"), "value" : 47 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfae"), "value" : 53 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfaf"), "value" : 52 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfb0"), "value" : 56 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfb1"), "value" : 54 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfb2"), "value" : 1 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfb3"), "value" : 35 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfb4"), "value" : 48 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfb5"), "value" : 94 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfb6"), "value" : 73 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfb7"), "value" : 33 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfb8"), "value" : 62 }
Type "it" for more
> it
{ "_id" : ObjectId("50778ce69331a280cf4bcfb9"), "value" : 44 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfba"), "value" : 37 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfbb"), "value" : 23 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfbc"), "value" : 29 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfbd"), "value" : 49 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfbe"), "value" : 0 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfbf"), "value" : 99 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfc0"), "value" : 2 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfc1"), "value" : 22 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfc2"), "value" : 22 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfc3"), "value" : 74 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfc4"), "value" : 57 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfc5"), "value" : 78 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfc6"), "value" : 35 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfc7"), "value" : 83 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfc8"), "value" : 85 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfc9"), "value" : 22 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfca"), "value" : 97 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfcb"), "value" : 63 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfcc"), "value" : 64 }
Type "it" for more
> it
{ "_id" : ObjectId("50778ce69331a280cf4bcfcd"), "value" : 31 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfce"), "value" : 72 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfcf"), "value" : 21 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfd0"), "value" : 59 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfd1"), "value" : 87 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfd2"), "value" : 10 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfd3"), "value" : 15 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfd4"), "value" : 95 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfd5"), "value" : 62 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfd6"), "value" : 68 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfd7"), "value" : 91 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfd8"), "value" : 6 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfd9"), "value" : 57 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfda"), "value" : 2 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfdb"), "value" : 60 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfdc"), "value" : 39 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfdd"), "value" : 46 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfde"), "value" : 6 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfdf"), "value" : 24 }
{ "_id" : ObjectId("50778ce69331a280cf4bcfe0"), "value" : 82 }
> exit
bye
u64@vm:~$ 
```

`hw1-2.py`

```python
#!/usr/bin/env python

import pymongo


# Copyright 2012-2016, 10gen, Inc.
# Author: Andrew Erlichson


# connect to the db on standard port
connection = pymongo.MongoClient("mongodb://localhost")



db = connection.m101                 # attach to db
collection = db.funnynumbers         # specify the collection


magic = 0

try:
    iter = collection.find()
    for item in iter:
        if ((item['value'] % 3) == 0):
            magic = magic + item['value']

except Exception as e:
    print "Error trying to read collection:", type(e), e


print "The answer to Homework One, Problem 2 is " + str(int(magic))
```

```sh
u64@vm:~/Desktop$ python hw1-2.py
The answer to Homework One, Problem 2 is 1815
u64@vm:~/Desktop$
```

![](images/2.png)

###### Breakdown of `hw1-2.py`

- `hw1-2.py` connect to the database `m101` and accesses the collection `funnynumbers`
- Then it iterates over the numbers stored in the the key `value`
- Checks if the numbers are divisible by `3`
- If so then it adds up all the numbers and prints the output