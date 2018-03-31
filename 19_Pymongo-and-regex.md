#### 19. Pymongo and regex

###### `using_regex.py`

```python
#!/usr/bin/env python
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.reddit
stories = db.stories


def find():

    print "find, reporting for duty"

    query = {'title': {'$regex': 'broadband|neutrality', '$options': 'i'}}
    projection = {'title': 1, '_id': 0}

    try:
        cursor = stories.find(query, projection)

    except Exception as e:
        print "Unexpected error:", type(e), e

    for doc in cursor:
        print doc

if __name__ == '__main__':
    find()
```

```sh
u64@vm:~/Desktop$ python using_regex.py
find, reporting for duty
{u'title': u'Please don\u2019t take broadband away from poor people, Democrats tell FCC chair'}
{u'title': u'Republicans block state net neutrality bill'}
{u'title': u'Los Angeles Wants to Build Its Own Citywide Broadband Network - It would be one of the largest municipal broadband networks in the world. Now, Los Angeles is studying an aggressive plan to protect net neutrality.'}
{u'title': u'Ajit Pai faces heat over proposal to take away poor people\u2019s broadband plans'}
{u'title': u"Maine GOP Uses 'Trick' to Scuttle State Net Neutrality Effort"}
{u'title': u'ACLU urges cities to build public broadband to protect net neutrality'}
u64@vm:~/Desktop$
```