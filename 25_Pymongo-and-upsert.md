#### 25. Pymongo and upsert

###### `using_upsert.py`

```python
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")
db = connection.test
things = db.things

def using_upsert():

    print "updating with upsert"

    try:

        # lets remove all stuff from things
        things.drop()

        things.update_one({'thing':'apple'}, {'$set':{'color':'red'}}, upsert=True)
		things.update_many({'thing':'banana'}, {'$set':{'color':'yellow'}}, upsert=True)
        things.replace_one({'thing':'pear'}, {'color':'green'}, upsert=True)


        apple = things.find_one({'thing':'apple'})
        print "apple: ", apple
        banana = things.find_one({'thing':'banana'})
        print "banana: ", banana 
        pear = things.find_one({'thing':'pear'})
        print "pear: ", pear

    except Exception as e:
        print "Unexpected error:", type(e), e
        raise


using_upsert()
```

```sh
u64@vm:~/Desktop$ python using_upsert.py
updating with upsert
apple:  {u'color': u'red', u'thing': u'apple', u'_id': ObjectId('5abee9ad09c41a95745d8e2d')}
banana:  {u'color': u'yellow', u'thing': u'banana', u'_id': ObjectId('5abee9ad09c41a95745d8e2f')}
pear:  None
u64@vm:~/Desktop$
```