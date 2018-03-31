import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.students
grades = db.grades

# find lowest scores

def remove_score(_id):
	try:
		doc = grades.find_one({'_id': _id})
		print "removing score ", doc['score'], " for student ", doc['student_id']
		grades.remove({"_id":_id})

	except:
		print "Unexpected error", sys.exc_info()[0]
		raise

def remove_lowest():

	cursor = grades.find({'type':'homework'}).sort([('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)])

	student_id = -1;
	for entry in cursor:
		if (entry['student_id'] != student_id):
			remove_score(entry['_id'])
		student_id = entry['student_id']

remove_lowest()
