#### 23. Pymongo, update_one and update_many

###### `using_update.py`

```python
#!/usr/bin/env python
import pymongo
import datetime

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")


# add a review date to a single record using update_one
def add_review_date_using_update_one(student_id):

    print "updating record using update_one and $set"
    # get a handle to the school database
    db = connection.school
    scores = db.scores

    try:
        # get the doc
        score = scores.find_one({'student_id': student_id, 'type': 'homework'})
        print "before: ", score

        # update using set
        record_id = score['_id']
        result = scores.update_one({'_id': record_id},
                          {'$set': {'review_date': datetime.datetime.utcnow()}})
        print "num matched: ", result.matched_count

        score = scores.find_one({'_id': record_id})
        print "after: ", score

    except Exception:
        raise


# add a review date to all records
def add_review_dates_for_all():

    print "updating record using update_many and $set"
    # get a handle to the school database
    db = connection.school
    scores = db.scores

    try:
        # update all the docs
        result = scores.update_many(
            {}, {'$set': {'review_date': datetime.datetime.utcnow()}})
        print "num matched: ", result.matched_count

    except Exception:
        raise


if __name__ == '__main__':
    #add_review_date_using_update_one(1)
    add_review_dates_for_all()
```

```sh
u64@vm:~/Desktop$ python using_update.py
updating record using update_one and $set
before:  {u'student_id': 1.0, u'_id': ObjectId('5abec1903d87dea58b6db0af'), u'type': u'homework', u'score': 23.81944948617104}
num matched:  1
after:  {u'student_id': 1.0, u'_id': ObjectId('5abec1903d87dea58b6db0af'), u'type': u'homework', u'score': 23.81944948617104, u'review_date': datetime.datetime(2018, 3, 31, 1, 20, 42, 573000)}
u64@vm:~/Desktop$
```

```sh
u64@vm:~/Desktop$ python using_update.py
updating record using update_many and $set
num matched:  300
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
> db.scores.find().pretty()
{
	"_id" : ObjectId("5abec1903d87dea58b6db0ab"),
	"student_id" : 0,
	"type" : "exam",
	"score" : 98.41189138228054,
	"review_date" : ISODate("2018-03-31T01:21:15.048Z")
}
{
	"_id" : ObjectId("5abec1903d87dea58b6db0ac"),
	"student_id" : 0,
	"type" : "homework",
	"score" : 46.002158540718064,
	"review_date" : ISODate("2018-03-31T01:21:15.048Z")
}
{
	"_id" : ObjectId("5abec1903d87dea58b6db0ad"),
	"student_id" : 0,
	"type" : "quiz",
	"score" : 70.0849659584677,
	"review_date" : ISODate("2018-03-31T01:21:15.048Z")
}
{
	"_id" : ObjectId("5abec1903d87dea58b6db0ae"),
	"student_id" : 1,
	"type" : "exam",
	"score" : 99.20068727155608,
	"review_date" : ISODate("2018-03-31T01:21:15.048Z")
}
{
	"_id" : ObjectId("5abec1903d87dea58b6db0af"),
	"student_id" : 1,
	"type" : "homework",
	"score" : 23.81944948617104,
	"review_date" : ISODate("2018-03-31T01:21:15.048Z")
}
{
	"_id" : ObjectId("5abec1903d87dea58b6db0b0"),
	"student_id" : 1,
	"type" : "quiz",
	"score" : 95.45004734750097,
	"review_date" : ISODate("2018-03-31T01:21:15.048Z")
}
{
	"_id" : ObjectId("5abec1903d87dea58b6db0b1"),
	"student_id" : 2,
	"type" : "exam",
	"score" : 44.46288282494467,
	"review_date" : ISODate("2018-03-31T01:21:15.048Z")
}
{
	"_id" : ObjectId("5abec1903d87dea58b6db0b2"),
	"student_id" : 2,
	"type" : "homework",
	"score" : 18.567787692991555,
	"review_date" : ISODate("2018-03-31T01:21:15.048Z")
}
{
	"_id" : ObjectId("5abec1903d87dea58b6db0b3"),
	"student_id" : 2,
	"type" : "quiz",
	"score" : 65.83308579702958,
	"review_date" : ISODate("2018-03-31T01:21:15.048Z")
}
{
	"_id" : ObjectId("5abec1903d87dea58b6db0b4"),
	"student_id" : 3,
	"type" : "exam",
	"score" : 49.22677515380557,
	"review_date" : ISODate("2018-03-31T01:21:15.048Z")
}
{
	"_id" : ObjectId("5abec1903d87dea58b6db0b5"),
	"student_id" : 3,
	"type" : "homework",
	"score" : 33.036197827575265,
	"review_date" : ISODate("2018-03-31T01:21:15.048Z")
}
{
	"_id" : ObjectId("5abec1903d87dea58b6db0b6"),
	"student_id" : 3,
	"type" : "quiz",
	"score" : 91.15619644951728,
	"review_date" : ISODate("2018-03-31T01:21:15.048Z")
}
{
	"_id" : ObjectId("5abec1903d87dea58b6db0b7"),
	"student_id" : 4,
	"type" : "exam",
	"score" : 42.2188987598181,
	"review_date" : ISODate("2018-03-31T01:21:15.048Z")
}
{
	"_id" : ObjectId("5abec1903d87dea58b6db0b8"),
	"student_id" : 4,
	"type" : "homework",
	"score" : 49.06261992475709,
	"review_date" : ISODate("2018-03-31T01:21:15.048Z")
}
{
	"_id" : ObjectId("5abec1903d87dea58b6db0b9"),
	"student_id" : 4,
	"type" : "quiz",
	"score" : 14.942267471652293,
	"review_date" : ISODate("2018-03-31T01:21:15.048Z")
}
{
	"_id" : ObjectId("5abec1903d87dea58b6db0ba"),
	"student_id" : 5,
	"type" : "exam",
	"score" : 48.66760420673933,
	"review_date" : ISODate("2018-03-31T01:21:15.048Z")
}
{
	"_id" : ObjectId("5abec1903d87dea58b6db0bb"),
	"student_id" : 5,
	"type" : "homework",
	"score" : 8.563628038272054,
	"review_date" : ISODate("2018-03-31T01:21:15.048Z")
}
{
	"_id" : ObjectId("5abec1903d87dea58b6db0bc"),
	"student_id" : 5,
	"type" : "quiz",
	"score" : 4.843525776062407,
	"review_date" : ISODate("2018-03-31T01:21:15.048Z")
}
{
	"_id" : ObjectId("5abec1903d87dea58b6db0bd"),
	"student_id" : 6,
	"type" : "exam",
	"score" : 14.581851677050295,
	"review_date" : ISODate("2018-03-31T01:21:15.048Z")
}
{
	"_id" : ObjectId("5abec1903d87dea58b6db0be"),
	"student_id" : 6,
	"type" : "homework",
	"score" : 98.45429794240965,
	"review_date" : ISODate("2018-03-31T01:21:15.048Z")
}
Type "it" for more
>
```