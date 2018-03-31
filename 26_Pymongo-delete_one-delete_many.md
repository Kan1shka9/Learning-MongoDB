#### 26. Pymongo, `delete_one`, `delete_many`

###### `remove_student_data.py`

```python
import pymongo
import datetime
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# removes one student
def remove_student(student_id):

    # get a handle to the school database
    db=connection.school
    scores = db.scores

    try:

        result = scores.delete_one({'student_id':student_id})
	#result = scores.delete_many({'student_id':student_id})

        print "num removed: ", result.deleted_count

    except Exception as e:
        print "Exception: ", type(e), e

def find_student_data(student_id):
    # get a handle to the school database
    db=connection.school
    scores = db.scores

    print "Searching for student data for student with id = ", student_id
    try:
        docs = scores.find({'student_id':student_id})
        for doc in docs:
            print doc

    except Exception as e:
        print "Exception: ", type(e), e




remove_student(1)
find_student_data(1)
```

```sh
u64@vm:~/Desktop$ python remove_student_data.py
num removed:  1
Searching for student data for student with id =  1
{u'student_id': 1.0, u'_id': ObjectId('5abec1903d87dea58b6db0af'), u'type': u'homework', u'score': 23.81944948617104, u'review_date': datetime.datetime(2018, 3, 31, 1, 39, 53, 463000)}
{u'student_id': 1.0, u'_id': ObjectId('5abec1903d87dea58b6db0b0'), u'type': u'quiz', u'score': 95.45004734750097}
u64@vm:~/Desktop$
``` 

```sh
u64@vm:~/Desktop$ python remove_student_data.py
num removed:  2
Searching for student data for student with id =  1
u64@vm:~/Desktop$
```