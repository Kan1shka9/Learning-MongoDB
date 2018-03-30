#### 17. Pymongo and `$gt` and `$lt`

###### `find_using_gt_lt.py`

```python
#!/usr/bin/env python
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.school
scores = db.scores


def find():

    print "find, reporting for duty"

    query = {'type': 'exam', 'score': {'$gt': 50, '$lt': 70}}

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


if __name__ == '__main__':
    find()
```

```sh
u64@vm:~/Desktop$ python find_using_gt_lt.py
find, reporting for duty
{u'student_id': 8.0, u'_id': ObjectId('5abec1903d87dea58b6db0c3'), u'type': u'exam', u'score': 69.0432832342168}
{u'student_id': 11.0, u'_id': ObjectId('5abec1903d87dea58b6db0cc'), u'type': u'exam', u'score': 56.86863061042408}
{u'student_id': 12.0, u'_id': ObjectId('5abec1903d87dea58b6db0cf'), u'type': u'exam', u'score': 58.76175997400127}
{u'student_id': 14.0, u'_id': ObjectId('5abec1903d87dea58b6db0d5'), u'type': u'exam', u'score': 55.428772358930956}
{u'student_id': 18.0, u'_id': ObjectId('5abec1903d87dea58b6db0e1'), u'type': u'exam', u'score': 63.43132580011302}
{u'student_id': 22.0, u'_id': ObjectId('5abec1903d87dea58b6db0ed'), u'type': u'exam', u'score': 54.751495559232545}
{u'student_id': 30.0, u'_id': ObjectId('5abec1903d87dea58b6db105'), u'type': u'exam', u'score': 54.17551595760217}
{u'student_id': 31.0, u'_id': ObjectId('5abec1903d87dea58b6db108'), u'type': u'exam', u'score': 55.76856929923849}
{u'student_id': 32.0, u'_id': ObjectId('5abec1903d87dea58b6db10b'), u'type': u'exam', u'score': 69.81749416228531}
{u'student_id': 36.0, u'_id': ObjectId('5abec1903d87dea58b6db117'), u'type': u'exam', u'score': 61.73681755297955}
{u'student_id': 40.0, u'_id': ObjectId('5abec1903d87dea58b6db123'), u'type': u'exam', u'score': 65.29486527409179}
u64@vm:~/Desktop$
```