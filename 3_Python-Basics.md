#### 3. Python Basics

- [Strings and Concatenation](#strings-and-concatenation)
- [Lists](#lists)
- [Dictionary](#dictionary)
- [List and Dictionary](#list-and-dictionary)
- [For Loop](#for-loop)
- [While Loop](#while-loop)
- [Functions](#functions)
- [Exceptions](#exceptions)

```sh
☁  ~  python
Python 2.7.10 (default, Jul 15 2017, 17:16:57)
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```

###### Strings and Concatenation

```
>>> print("Hello, World!")
Hello, World!
>>> print("Hello " + "kan1shka9")
Hello kan1shka9
>>> print("Hello " + "kanishka" + " sunnam")
Hello kanishka sunnam
>>>
```

###### Lists

```
>>> a = ["orange", "apple", "banana"]
>>> a
['orange', 'apple', 'banana']
>>> print(a)
['orange', 'apple', 'banana']
>>>
```

```
>>> b = [1,2,3]
>>> b
[1, 2, 3]
>>> print(b)
[1, 2, 3]
>>>
```

```
>>> c = [1, ['orange', 'apple', 'banana'], 3]
>>> c
[1, ['orange', 'apple', 'banana'], 3]
>>> print(c)
[1, ['orange', 'apple', 'banana'], 3]
>>> print(c[1])
['orange', 'apple', 'banana']
>>> print(c[0])
1
>>> print(c[2])
3
>>>
```

```
>>> a = [0,1,2,3,4,5]
>>> a[0:3]
[0, 1, 2]
>>> a[2:3]
[2]
>>> a[2:]
[2, 3, 4, 5]
>>> a[:6]
[0, 1, 2, 3, 4, 5]
>>> a[:]
[0, 1, 2, 3, 4, 5]
>>>
```

```
>>> a = ['apple', 'pear', 'oranges']
>>> 'pear' in a
True
>>> 'grape' in a
False
>>> if 'pear' in a:
...     print("There is a pear")
...
There is a pear
>>> if 'grape' in a:
...     print("There is a grape")
...
>>>
```

###### Dictionary

```
>>> g = {'name': 'Kanishka Sunnam', 'city_of_birth': 'Vizag'}
>>> g
{'city_of_birth': 'Vizag', 'name': 'Kanishka Sunnam'}
>>> g['name']
'Kanishka Sunnam'
>>> g['name'] = "kan1shka9"
>>> g
{'city_of_birth': 'Vizag', 'name': 'kan1shka9'}
>>> g.keys()
['city_of_birth', 'name']
>>> del(g['name'])
>>> g
{'city_of_birth': 'Vizag'}
>>> del(g['foo'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'foo'
>>> 'city_of_birth' in g
True
>>> 'foo' in g
False
>>>
```

###### List and Dictionary

```
>>> a = {"name":"kanishka sunnam", "interests":["cycling", "running", "golf"]}
>>> a
{'interests': ['cycling', 'running', 'golf'], 'name': 'kanishka sunnam'}
>>> a["interests"][1]
'running'
>>> a["interests"].append("swimming")
>>> a
{'interests': ['cycling', 'running', 'golf', 'swimming'], 'name': 'kanishka sunnam'}
>>>
```

###### For Loop

- **Loops with `list`**

`loops.py`

```python
fruit = ['apple', 'orange', 'grape'] # init the array

new_fruit = []

for item in fruit:	# iterate
	print item

	new_fruit.append(item)

print new_fruit
```

```sh
☁  python [master] ⚡ python loops.py
apple
orange
grape
['apple', 'orange', 'grape']
☁  python [master] ⚡
```

`loops_2.py`

```python
sum = 0
numbers = [1, 2, 3, 5, 8]
for i in numbers:
    sum = sum + i
print i
```

```sh
☁  python [master] ⚡ python loops_2.py
8
☁  python [master] ⚡
```

- **Loops with `dict`**

`loops_3.py`

```python
person = {'name':'Kanishka Sunnam', 'fav_color': 'white', 'hair': 'black'} # init a dict

for key in person:	# iterate
	print "key is " + key + ", value is " + person[key]
```

```sh
☁  python [master] ⚡ python loops_3.py
key is hair, value is black
key is fav_color, value is white
key is name, value is Kanishka Sunnam
☁  python [master] ⚡
```

`loops_4.py`

```python
people = {'name': 'Bob', 'hometown': "Palo Alto", 'favorite_color': 'red'}
for item in people:
    if (item == 'favorite_color'):
        print people[item]
```

```sh
☁  python [master] ⚡ python loops_4.py
red
☁  python [master] ⚡
```

###### While loop

`loops_5.py`

```python
fruit = ['apple', 'orange', 'grape']	# init the array

i = 0
while (i < len(fruit)):
	print fruit[i]
	i = i + 1
```

```sh
☁  python [master] ⚡ python loops_5.py
apple
orange
grape
☁  python [master] ⚡
```

###### Functions

`functions.py`

```python
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
```

```sh
☁  python [master] ⚡ python functions.py
{'orange': 2, 'kiwi': 1, 'grape': 1, 'apple': 2}
☁  python [master] ⚡
```

###### Exceptions

`exception_uncaught.py`

```python
print 5 / 0

print "but life goes on"
```

```sh
☁  python [master] ⚡ python exception_uncaught.py
Traceback (most recent call last):
  File "exception_uncaught.py", line 1, in <module>
    print 5 / 0
ZeroDivisionError: integer division or modulo by zero
☁  python [master] ⚡
```

`exception_caught.py`

```python
import sys

try:
    print 5 / 0
except Exception as e:
    print "exception: ", type(e), e

print "but life goes on"
```

```sh
☁  python [master] ⚡ python exception_caught.py
exception:  <type 'exceptions.ZeroDivisionError'> integer division or modulo by zero
but life goes on
☁  python [master] ⚡
```
