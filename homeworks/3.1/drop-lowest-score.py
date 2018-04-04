#!/usr/bin/env python
"""
Drops the lowest score for each student in the collection.

Usage:
    python drop_lowest.py
"""

from pymongo import MongoClient
from sys import exc_info


def find_lowest_hw(scores):
    """
    Finds lowest hw score in the list.
    """
    lowest = None
    lowest_score = 101
    for item in scores:
        if ((item['type'] == "homework") and (item['score'] < lowest_score)):
            # found a new bound
            lowest = item
            lowest_score = lowest['score']

    return lowest


def remove_lowest(collection):
    """
    Drops the lowest score for each student.
    """
    cursor = collection.find()
    for student in cursor:
        _id = student["_id"]
        print "Looking at student {_id}:".format(_id=_id)
        scores = student['scores']
        lowest = find_lowest_hw(scores)
        if (lowest is not None):
            print ("  Removing hw grade of {score}."
                   ).format(score=lowest['score'])
            scores.remove(lowest)
            collection.update_one({'_id': _id},
                                  {'$set': {'scores': scores}})
        else:
            print "  Could not find a homework score to process"


def main():
    """
    Establishes a client and drops the lowest score for each student.
    """
    host = 'localhost'
    port = 27017
    dbname = 'school'
    collname = 'students'

    client = MongoClient(host=host, port=port)
    db = client[dbname]
    collection = db[collname]

    print ("Removing lowest score from students in the {db}.{collection} "
           "namespace."
           ).format(db=db.name, collection=collection.name)
    remove_lowest(collection=collection)


if __name__ == '__main__':
    main()