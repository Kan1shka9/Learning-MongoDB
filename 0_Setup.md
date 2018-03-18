#### 0. Setup

- [Install `MongoDB` Community Edition on `Ubuntu`](https://docs.mongodb.com/getting-started/shell/tutorial/install-mongodb-on-ubuntu/)
- [Install `pip`]()
- [Install `pymongo`]()
	- [`PyMongo`](https://api.mongodb.com/python/current/)
- [Install `bottle`]()
	- [`Bottle: Python Web Framework`](https://bottlepy.org/docs/dev/)

###### Install `MongoDB` Community Edition on `Ubuntu`

```sh
sudo service mongod start
```

```sh
u64@vm:~$ mongod
2018-03-12T10:38:39.460-0700 I CONTROL  [initandlisten] MongoDB starting : pid=4447 port=27017 dbpath=/data/db 64-bit host=vm
2018-03-12T10:38:39.460-0700 I CONTROL  [initandlisten] db version v3.6.3
2018-03-12T10:38:39.461-0700 I CONTROL  [initandlisten] git version: 9586e557d54ef70f9ca4b43c26892cd55257e1a5
2018-03-12T10:38:39.461-0700 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.0.2g  1 Mar 2016
2018-03-12T10:38:39.461-0700 I CONTROL  [initandlisten] allocator: tcmalloc
2018-03-12T10:38:39.462-0700 I CONTROL  [initandlisten] modules: none
2018-03-12T10:38:39.462-0700 I CONTROL  [initandlisten] build environment:
2018-03-12T10:38:39.462-0700 I CONTROL  [initandlisten]     distmod: ubuntu1604
2018-03-12T10:38:39.463-0700 I CONTROL  [initandlisten]     distarch: x86_64
2018-03-12T10:38:39.463-0700 I CONTROL  [initandlisten]     target_arch: x86_64
2018-03-12T10:38:39.463-0700 I CONTROL  [initandlisten] options: {}
2018-03-12T10:38:39.464-0700 I STORAGE  [initandlisten] exception in initAndListen: IllegalOperation: Attempted to create a lock file on a read-only directory: /data/db, terminating
2018-03-12T10:38:39.464-0700 I CONTROL  [initandlisten] now exiting
2018-03-12T10:38:39.464-0700 I CONTROL  [initandlisten] shutting down with code:100
u64@vm:~$
```

```sh
u64@vm:~$ mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
Server has startup warnings:
2018-03-12T10:26:42.962-0700 I STORAGE  [initandlisten]
2018-03-12T10:26:42.962-0700 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2018-03-12T10:26:42.962-0700 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2018-03-12T10:26:44.058-0700 I CONTROL  [initandlisten]
2018-03-12T10:26:44.058-0700 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2018-03-12T10:26:44.058-0700 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2018-03-12T10:26:44.058-0700 I CONTROL  [initandlisten]
2018-03-12T10:26:44.058-0700 I CONTROL  [initandlisten]
2018-03-12T10:26:44.058-0700 I CONTROL  [initandlisten] ** WARNING: /sys/kernel/mm/transparent_hugepage/enabled is 'always'.
2018-03-12T10:26:44.058-0700 I CONTROL  [initandlisten] **        We suggest setting it to 'never'
2018-03-12T10:26:44.058-0700 I CONTROL  [initandlisten]
> db
test
> db.names.insert({'name':'First'})
WriteResult({ "nInserted" : 1 })
> db.names.find()
{ "_id" : ObjectId("5aa6b8ab2d73ad01e64e8d61"), "name" : "First" }
>
bye
u64@vm:~$
```

###### Install `pip`

```sh
sudo apt install python-pip
pip install --upgrade pip
```

###### Install `pymongo`

```sh
pip install pymongo
```

```sh
u64@vm:~$ mongod
2018-03-17T20:54:21.390-0700 I CONTROL  [initandlisten] MongoDB starting : pid=52312 port=27017 dbpath=/data/db 64-bit host=vm
2018-03-17T20:54:21.391-0700 I CONTROL  [initandlisten] db version v3.6.3
2018-03-17T20:54:21.391-0700 I CONTROL  [initandlisten] git version: 9586e557d54ef70f9ca4b43c26892cd55257e1a5
2018-03-17T20:54:21.392-0700 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.0.2g  1 Mar 2016
2018-03-17T20:54:21.392-0700 I CONTROL  [initandlisten] allocator: tcmalloc
2018-03-17T20:54:21.392-0700 I CONTROL  [initandlisten] modules: none
2018-03-17T20:54:21.393-0700 I CONTROL  [initandlisten] build environment:
2018-03-17T20:54:21.393-0700 I CONTROL  [initandlisten]     distmod: ubuntu1604
2018-03-17T20:54:21.393-0700 I CONTROL  [initandlisten]     distarch: x86_64
2018-03-17T20:54:21.394-0700 I CONTROL  [initandlisten]     target_arch: x86_64
2018-03-17T20:54:21.394-0700 I CONTROL  [initandlisten] options: {}
2018-03-17T20:54:21.410-0700 I STORAGE  [initandlisten] exception in initAndListen: IllegalOperation: Attempted to create a lock file on a read-only directory: /data/db, terminating
2018-03-17T20:54:21.412-0700 I CONTROL  [initandlisten] now exiting
2018-03-17T20:54:21.412-0700 I CONTROL  [initandlisten] shutting down with code:100
u64@vm:~$
```

``pymongo_getting_started.py``

```python
import pymongo

from pymongo import MongoClient

# connect to database
connection = MongoClient('localhost', 27017)

db = connection.test

# handle to names collection
names = db.names

item = names.find_one()

print item['name']
```

```sh
u64@vm:~$ python pymongo_getting_started.py
First
u64@vm:~$
```

###### Install `bottle`

```
pip install bottle
```