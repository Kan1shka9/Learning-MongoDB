#### 27. Pymongo, find and modify

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
> db.counters.find()
>
bye
u64@vm:~/Desktop$
```

###### `using_find_and_modify.py`

```python
import pymongo

# gets the next number in a sequence
def get_next_sequence_number(name):
    connection = pymongo.MongoClient("mongodb://localhost")

    db = connection.test
    counters = db.counters

    # let's get ourselves a sequence number
    # note there are two other varients of this call as well:
    # find_one_and_delete
    # find_one_and_replace
    # all these map to the the command find_and_modify


    try:
        counter = counters.find_one_and_update(filter={'type':name},
                                               update={'$inc':{'value':-1}},
                                               upsert=True,
                                               return_document=pymongo.ReturnDocument.AFTER)
    except Exception as e:
        print "Exception: ", type(e), e

    counter_value = counter['value']
    return counter_value


print get_next_sequence_number('uid')
print get_next_sequence_number('uid')
print get_next_sequence_number('uid')
```

```sh
u64@vm:~/Desktop$ python using_find_and_modify.py
-1
-2
-3
u64@vm:~/Desktop$
```

```sh
u64@vm:~/Desktop$ python using_find_and_modify.py
-4
-5
-6
u64@vm:~/Desktop$
```

```sh
u64@vm:~/Desktop$ python using_find_and_modify.py
-7
-8
-9
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
> db.counters.find()
{ "_id" : ObjectId("5abf205809c41a95745d8e6c"), "type" : "uid", "value" : -9 }
>
bye
u64@vm:~/Desktop$
```