#### 3. Python Basics

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

###### Loops

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