#### 0. Setup

- [Install `MongoDB` Community Edition on `Ubuntu`](https://docs.mongodb.com/getting-started/shell/tutorial/install-mongodb-on-ubuntu/)
- [Install `pip`](#install-pip)
- [Install `pymongo`](#install-pymongo)
	- [`PyMongo`](https://api.mongodb.com/python/current/)
- [Install `bottle`](#install-bottle)
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
u64@vm:~$ sudo service mongod start
[sudo] password for u64:
u64@vm:~$ pgrep mongo
3417
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

`bottle_getting_started.py`

```python
from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)
```

```sh
u64@vm:~$ python bottle_getting_started.py
Bottle v0.12.13 server starting up (using WSGIRefServer())...
Listening on http://localhost:8080/
Hit Ctrl-C to quit.

127.0.0.1 - - [18/Mar/2018 09:42:24] "GET / HTTP/1.1" 404 720
127.0.0.1 - - [18/Mar/2018 09:42:24] "GET /favicon.ico HTTP/1.1" 404 742
127.0.0.1 - - [18/Mar/2018 09:42:39] "GET / HTTP/1.1" 404 720
127.0.0.1 - - [18/Mar/2018 09:42:39] "GET /favicon.ico HTTP/1.1" 404 742
127.0.0.1 - - [18/Mar/2018 09:43:58] "GET /hello/kan1shka9 HTTP/1.1" 200 23
```

```
http://localhost:8080/hello/kan1shka9
```

![](images/0/1.png)
