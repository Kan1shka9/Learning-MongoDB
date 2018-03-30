#### 16. Pymongo and Projections

###### `using_find_with_projection.py`

```python
#!/usr/bin/env python
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.school
scores = db.scores


def find():

    print "find, reporting for duty"

    query = {'type': 'exam'}
    projection = {'student_id': 1, '_id': 0}
#   projection = {'student_id': 1}

    try:
        cursor = scores.find(query, projection)

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
u64@vm:~/Desktop$ python using_find_with_projection.py
find, reporting for duty
{u'student_id': 0.0}
{u'student_id': 1.0}
{u'student_id': 2.0}
{u'student_id': 3.0}
{u'student_id': 4.0}
{u'student_id': 5.0}
{u'student_id': 6.0}
{u'student_id': 7.0}
{u'student_id': 8.0}
{u'student_id': 9.0}
{u'student_id': 10.0}
u64@vm:~/Desktop$
```

```sh
u64@vm:~/Desktop$ python using_find_with_projection.py
find, reporting for duty
{u'student_id': 0.0, u'_id': ObjectId('5abec1903d87dea58b6db0ab')}
{u'student_id': 1.0, u'_id': ObjectId('5abec1903d87dea58b6db0ae')}
{u'student_id': 2.0, u'_id': ObjectId('5abec1903d87dea58b6db0b1')}
{u'student_id': 3.0, u'_id': ObjectId('5abec1903d87dea58b6db0b4')}
{u'student_id': 4.0, u'_id': ObjectId('5abec1903d87dea58b6db0b7')}
{u'student_id': 5.0, u'_id': ObjectId('5abec1903d87dea58b6db0ba')}
{u'student_id': 6.0, u'_id': ObjectId('5abec1903d87dea58b6db0bd')}
{u'student_id': 7.0, u'_id': ObjectId('5abec1903d87dea58b6db0c0')}
{u'student_id': 8.0, u'_id': ObjectId('5abec1903d87dea58b6db0c3')}
{u'student_id': 9.0, u'_id': ObjectId('5abec1903d87dea58b6db0c6')}
{u'student_id': 10.0, u'_id': ObjectId('5abec1903d87dea58b6db0c9')}
u64@vm:~/Desktop$
```