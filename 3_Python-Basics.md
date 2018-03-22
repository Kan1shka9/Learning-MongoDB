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