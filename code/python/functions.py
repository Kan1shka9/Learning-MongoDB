fruit = ['apple', 'orange', 'grape', 'kiwi', 'orange', 'apple'] # init the array

# reports the frequency of every item in a list
def analyze_list(l):

	counts = {} # init an empty dict
	for item in l:
		if item in counts:
			counts[item] = counts[item] + 1
		else:
			counts[item] = 1 
	return counts

# lets analyze a list
counts = analyze_list(fruit)
print counts
