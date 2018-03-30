#### 15. Pymongo, find_one() and find()

###### `create_student_collection.js`

```javascript
use school
db.scores.drop();
var types = ['exam', 'homework', 'quiz']
for (student_id = 0; student_id < 100; student_id++) {
    for (type=0; type < 3; type++) {
    var r = {'student_id':student_id, 'type':types[type], 'score':Math.random() * 100};
    db.scores.insert(r);
    }
}
```

```sh
u64@vm:~/Desktop$ mongo < create_student_collection.js
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db school
true
WriteResult({ "nInserted" : 1 })
bye
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
school  0.000GB
> use school
switched to db school
> show collections
scores
>
```

```
> db.scores.find()
{ "_id" : ObjectId("5abec0653cf030334e0f71e2"), "student_id" : 0, "type" : "exam", "score" : 50.20613469865518 }
{ "_id" : ObjectId("5abec0653cf030334e0f71e3"), "student_id" : 0, "type" : "homework", "score" : 37.67108686046814 }
{ "_id" : ObjectId("5abec0653cf030334e0f71e4"), "student_id" : 0, "type" : "quiz", "score" : 56.55278328356954 }
{ "_id" : ObjectId("5abec0653cf030334e0f71e5"), "student_id" : 1, "type" : "exam", "score" : 47.94070444662201 }
{ "_id" : ObjectId("5abec0653cf030334e0f71e6"), "student_id" : 1, "type" : "homework", "score" : 58.112287660484554 }
{ "_id" : ObjectId("5abec0653cf030334e0f71e7"), "student_id" : 1, "type" : "quiz", "score" : 85.67431017668959 }
{ "_id" : ObjectId("5abec0653cf030334e0f71e8"), "student_id" : 2, "type" : "exam", "score" : 22.1968413695693 }
{ "_id" : ObjectId("5abec0653cf030334e0f71e9"), "student_id" : 2, "type" : "homework", "score" : 29.65134088753555 }
{ "_id" : ObjectId("5abec0653cf030334e0f71ea"), "student_id" : 2, "type" : "quiz", "score" : 14.307176630159478 }
{ "_id" : ObjectId("5abec0653cf030334e0f71eb"), "student_id" : 3, "type" : "exam", "score" : 8.413349268163339 }
{ "_id" : ObjectId("5abec0653cf030334e0f71ec"), "student_id" : 3, "type" : "homework", "score" : 87.55688440313268 }
{ "_id" : ObjectId("5abec0653cf030334e0f71ed"), "student_id" : 3, "type" : "quiz", "score" : 15.160380759996794 }
{ "_id" : ObjectId("5abec0653cf030334e0f71ee"), "student_id" : 4, "type" : "exam", "score" : 7.900902206592475 }
{ "_id" : ObjectId("5abec0653cf030334e0f71ef"), "student_id" : 4, "type" : "homework", "score" : 71.60569523199396 }
{ "_id" : ObjectId("5abec0653cf030334e0f71f0"), "student_id" : 4, "type" : "quiz", "score" : 43.50855909253274 }
{ "_id" : ObjectId("5abec0653cf030334e0f71f1"), "student_id" : 5, "type" : "exam", "score" : 76.15944338930527 }
{ "_id" : ObjectId("5abec0653cf030334e0f71f2"), "student_id" : 5, "type" : "homework", "score" : 79.87789315164821 }
{ "_id" : ObjectId("5abec0653cf030334e0f71f3"), "student_id" : 5, "type" : "quiz", "score" : 25.644246136368753 }
{ "_id" : ObjectId("5abec0653cf030334e0f71f4"), "student_id" : 6, "type" : "exam", "score" : 61.79461705762934 }
{ "_id" : ObjectId("5abec0653cf030334e0f71f5"), "student_id" : 6, "type" : "homework", "score" : 65.7564084472226 }
Type "it" for more
> it
{ "_id" : ObjectId("5abec0653cf030334e0f71f6"), "student_id" : 6, "type" : "quiz", "score" : 15.498684317287282 }
{ "_id" : ObjectId("5abec0653cf030334e0f71f7"), "student_id" : 7, "type" : "exam", "score" : 71.96455733409007 }
{ "_id" : ObjectId("5abec0653cf030334e0f71f8"), "student_id" : 7, "type" : "homework", "score" : 18.66462026314908 }
{ "_id" : ObjectId("5abec0653cf030334e0f71f9"), "student_id" : 7, "type" : "quiz", "score" : 84.54017988110273 }
{ "_id" : ObjectId("5abec0653cf030334e0f71fa"), "student_id" : 8, "type" : "exam", "score" : 88.2982445205485 }
{ "_id" : ObjectId("5abec0653cf030334e0f71fb"), "student_id" : 8, "type" : "homework", "score" : 74.57469125998945 }
{ "_id" : ObjectId("5abec0653cf030334e0f71fc"), "student_id" : 8, "type" : "quiz", "score" : 20.60749219563981 }
{ "_id" : ObjectId("5abec0653cf030334e0f71fd"), "student_id" : 9, "type" : "exam", "score" : 98.3017555676157 }
{ "_id" : ObjectId("5abec0653cf030334e0f71fe"), "student_id" : 9, "type" : "homework", "score" : 2.871554387699715 }
{ "_id" : ObjectId("5abec0653cf030334e0f71ff"), "student_id" : 9, "type" : "quiz", "score" : 98.19467617129372 }
{ "_id" : ObjectId("5abec0653cf030334e0f7200"), "student_id" : 10, "type" : "exam", "score" : 51.58838681908845 }
{ "_id" : ObjectId("5abec0653cf030334e0f7201"), "student_id" : 10, "type" : "homework", "score" : 97.65668930304005 }
{ "_id" : ObjectId("5abec0653cf030334e0f7202"), "student_id" : 10, "type" : "quiz", "score" : 88.76110331639518 }
{ "_id" : ObjectId("5abec0653cf030334e0f7203"), "student_id" : 11, "type" : "exam", "score" : 2.4152493746325554 }
{ "_id" : ObjectId("5abec0653cf030334e0f7204"), "student_id" : 11, "type" : "homework", "score" : 15.001492855615906 }
{ "_id" : ObjectId("5abec0653cf030334e0f7205"), "student_id" : 11, "type" : "quiz", "score" : 68.34222932236784 }
{ "_id" : ObjectId("5abec0653cf030334e0f7206"), "student_id" : 12, "type" : "exam", "score" : 95.52617004997515 }
{ "_id" : ObjectId("5abec0653cf030334e0f7207"), "student_id" : 12, "type" : "homework", "score" : 49.75605752670306 }
{ "_id" : ObjectId("5abec0653cf030334e0f7208"), "student_id" : 12, "type" : "quiz", "score" : 59.01748983304219 }
{ "_id" : ObjectId("5abec0653cf030334e0f7209"), "student_id" : 13, "type" : "exam", "score" : 70.96490318163723 }
Type "it" for more
>
```

```
> db.scores.findOne()
{
	"_id" : ObjectId("5abec1903d87dea58b6db0ab"),
	"student_id" : 0,
	"type" : "exam",
	"score" : 98.41189138228054
}
>
```

###### `using_find.py`

```python
#!/usr/bin/env python
import pymongo

# It is not necessary to import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.school
scores = db.scores


def find():

    print "find(), reporting for duty"

    query = {'type': 'exam'}

    try:
        cursor = scores.find(query)

    except Exception as e:
        print "Unexpected error:", type(e), e

    sanity = 0
    for doc in cursor:
        print doc
        sanity += 1
        if (sanity > 10):
            break


def find_one():

    print "find_one(), reporting for duty"
    query = {'student_id': 10}
    
    try:
        doc = scores.find_one(query)
        
    except Exception as e:
        print "Unexpected error:", type(e), e
    
    print doc


if __name__ == '__main__':
    find()  # Change this to find_one() to run that function, instead.
```

- `find_one()`

```sh
u64@vm:~/Desktop$ python using_find.py
find_one(), reporting for duty
{u'student_id': 10.0, u'_id': ObjectId('5abec1903d87dea58b6db0c9'), u'type': u'exam', u'score': 20.917576229877245}
u64@vm:~/Desktop$
```

- `find()`

```sh
u64@vm:~/Desktop$ python using_find.py
find(), reporting for duty
{u'student_id': 0.0, u'_id': ObjectId('5abec1903d87dea58b6db0ab'), u'type': u'exam', u'score': 98.41189138228054}
{u'student_id': 1.0, u'_id': ObjectId('5abec1903d87dea58b6db0ae'), u'type': u'exam', u'score': 99.20068727155608}
{u'student_id': 2.0, u'_id': ObjectId('5abec1903d87dea58b6db0b1'), u'type': u'exam', u'score': 44.46288282494467}
{u'student_id': 3.0, u'_id': ObjectId('5abec1903d87dea58b6db0b4'), u'type': u'exam', u'score': 49.22677515380557}
{u'student_id': 4.0, u'_id': ObjectId('5abec1903d87dea58b6db0b7'), u'type': u'exam', u'score': 42.2188987598181}
{u'student_id': 5.0, u'_id': ObjectId('5abec1903d87dea58b6db0ba'), u'type': u'exam', u'score': 48.66760420673933}
{u'student_id': 6.0, u'_id': ObjectId('5abec1903d87dea58b6db0bd'), u'type': u'exam', u'score': 14.581851677050295}
{u'student_id': 7.0, u'_id': ObjectId('5abec1903d87dea58b6db0c0'), u'type': u'exam', u'score': 36.57093842577369}
{u'student_id': 8.0, u'_id': ObjectId('5abec1903d87dea58b6db0c3'), u'type': u'exam', u'score': 69.0432832342168}
{u'student_id': 9.0, u'_id': ObjectId('5abec1903d87dea58b6db0c6'), u'type': u'exam', u'score': 10.759764782798909}
{u'student_id': 10.0, u'_id': ObjectId('5abec1903d87dea58b6db0c9'), u'type': u'exam', u'score': 20.917576229877245}
u64@vm:~/Desktop$
```