#### 20. Pymongo, Skip, Sort, Limit

###### Order

- Sort
- Skip
- Limit

###### `using_limit_skip_sort.py`

```python
#!/usr/bin/env python
import pymongo

# no need to import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.school
scores = db.scores


def find():
    print "find, reporting for duty"
    query = {}
    try:
        cursor = scores.find(query).skip(4)
        cursor.limit(1)

        # Sorting using single key
#        cursor.sort('student_id', pymongo.ASCENDING).skip(4).limit(1)

        # Sorting using multiple key
        cursor.sort([('student_id', pymongo.ASCENDING), ('score', pymongo.DESCENDING)])

    except Exception as e:
        print "Unexpected error:", type(e), e

    for doc in cursor:
        print doc


if __name__ == '__main__':
    find()
```

```sh
u64@vm:~/Desktop$ python using_limit_skip_sort.py
find, reporting for duty
{u'student_id': 1.0, u'_id': ObjectId('5abec1903d87dea58b6db0b0'), u'type': u'quiz', u'score': 95.45004734750097}
u64@vm:~/Desktop$
```
