# 2. Python Object and Data Structure Basics

## Python Data Types
| Name | Data type | Description |
| ----------- | ----------- | ----------- |
| Integers | int | Whole numbers, such as 300 |
| Floating point | float | Numbers with a decimal point, such as 2.3 |
| Strings | str | Ordered sequence of characters, such as "Hello", '20' |
| Lists | list | Ordered sequence of objects: [10, "Hi", 2.3] |
| Dictionaries | dict | Unordered key:value pairs: {"key1":"val1", "key2":"value2"} |
| Tuples | tup | Ordered immutable sequence of objects: (10, "hi", 2.3) |
| Sets | set | Unordered collection of unique objects: {"a", "b"} |
| Booleans | bool | Logical value indicating True or False |

### Python numbers
```py
print(2 + 1) # 3 # plus
print(2 - 1) # 1 # minus
print(2 * 2) # 4 # multiply
print(2 / 3) # 0.6666666666666666 # divide
print(7 % 4 ) # 3 # Modulo
print((-7) % 3) # 2
print(2 ** 3) # 8 # power

print(0.1+0.2) # 0.30000000000000004 # approximation with decimal
print(round(2.675, 2)) # 2.67 # round the value 2.675 to two decimal places

from decimal import Decimal
print(Decimal(2.675)) # to see the exact value
# Decimal('2.67499999999999982236431605997495353221893310546875')
```

No matter how many base 2 digits you’re willing to use, the decimal value 0.1 cannot be represented exactly as a base 2 fraction. In base 2, 1/10 is the infinitely repeating fraction. On a typical machine running Python, there are 53 bits of precision available for a Python float. Refer to `https://docs.python.org/2/tutorial/floatingpoint.html`. 

It’s easy to forget that the stored value is an approximation to the original decimal fraction, because of the way that floats are displayed at the interpreter prompt.

Since the decimal fraction 2.675 is exactly halfway between 2.67 and 2.68, you might expect the result here to be (a binary approximation to) 2.68. It’s not, because when the decimal string 2.675 is converted to a binary floating-point number, it’s again replaced with a binary approximation, whose exact value is 2.67499999999999982236431605997495353221893310546875. 

If you’re in a situation where you care which way your decimal halfway-cases are rounded, you should consider using the decimal module, which provides a nice way to “see” the exact value that’s stored in any particular Python float. 

Still, don’t be unduly wary of floating-point! The errors in Python float operations are inherited from the floating-point hardware, and on most machines are on the order of no more than 1 part in `2**53` per operation. That’s more than adequate for most tasks, but you do need to keep in mind that it’s not decimal arithmetic, and that every float operation can suffer a new rounding error.

While pathological cases do exist, for most casual use of floating-point arithmetic you’ll see the result you expect in the end if you simply round the display of your final results to the number of decimal digits you expect.

### Variable Assignments
It is considered best practice that `names are lower case`, except for global variables. 

Python uses `Dynamic Typing`, which means you can reassign variables to different data types. It makes Python flexible in assigning data types, different than other languages that are Statically-Typed. Something like this is okay in Python:
```python
my_dogs = 2
my_dogs = ["Sammy", "Frankie"]
```

```py
a = 5
print(a) # 5
a =  a + a 
print(a) # 10
print(type(a)) # <class 'int'> # return type of a variable
a = 3.2 # example of dynamic typing
print(type(a)) # <class 'float'>

income = 3
tax_rate = 0.2
tax_amount = income * tax_rate
print(tax_amount) # 0.6000000000000001
```

Pros of Dynamic Typing: Easy to work with; Faster development time.

Const of Dynamic Typing: May result in bugs for unexpected data types; You need to be aware of `type()`. 

### Strings
Strings are ordered sequences of characters using the syntax of single quotes or double quotes. The nice thing about having two choices is that if you have one type of quote in your string that you want to keep, you can use the other type of quote to wrap it, such as `"I don't know. "`. 

Python also use reverse indexing: 
```
Character:     h  e  l  l  o
Index:         0  1  2  3  4
Reverse Index: 0 -1 -3 -2 -1
```
### Indexing and Slicing with Strings
```py
print('hello, this is a string') 
print("I'm learning python. ") # take advantage of single or double quotes
print('hello\nworld') # have a new line in a string
# hello
# world
print('hello\tworld') # hello   world # have a tab in a string
print(len('hello round')) # 11 # length of string

s = "Hello World!"
print(s[0]) # H # get a char out of string
print(s[-3]) # l # reverse indexing
print(s[2:]) # llo World! # get substr starting at idx=2
print(s[:2]) # He # get the substr up to but exclusive idx=2
print(s[2:5]) # llo # get the substr start at idx=2 and ends at idx=5 (exclusive)
print(s[::]) # Hello World! # get the whole string, with step size unspecified
print(s[::2]) # HloWrd # get the whole string with step size=2
print(s[2:7:2]) # loW # get the substring idx = [2, 7) with step size=2. [start:stop:step size]
print(s[::-1]) # !dlroW olleH # reverse the string
```

### String Properties and Methods
```py
name = 'Sam'
# name[0] = 'P' # TypeError due to string is immutable. So if want to change it, will need to create a new string
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# /var/folders/bn/yypl5g397pz61ngtbr4xsbrc0000gn/T/ipykernel_78033/1930518064.py in 
# ----> 1 name[0] = 'P' # TypeError due to string is immutable
#       2 # So if want to change it, will need to create a new string.

# TypeError: 'str' object does not support item assignment
name2 = 'P' + name[1:] # string concatenation
print(name2) # Pam
name3 = name * 5 # multiplication of strings
print(name3) # SamSamSamSamSam
print(name.upper()) # SAM # convert to upper case. Returns the new string
print("NAME".lower()) # name # convert to lower case
print("Hello World!".split()) # ['Hello', 'World!'] # split a string by space, return a list
print("Hello World!".split("o")) # ['Hell', ' W', 'rld!'] # split by specified string
print("Hello World!".split("o ")) # ['Hell', 'World!'] # split by specified string
```

### Print formatting with strings
```py
print('This is a string {}'.format('INSERTED')) # This is a string INSERTED # String interpolation (insert a var into a string)
print('The {} {} {}'.format('round1', 'round2', 'round3')) # The round1 round2 round3
print('The {2} {1} {0}'.format('round1', 'round2', 'round3')) # The round3 round2 round1 # reorder
print('The {0} {0} {0}'.format('round1', 'round2', 'round3')) # The round1 round1 round1 # repeat
print('The {r1} {r2} {r3}'.format(r1='round1', r2='round2', r3='round3')) # The round1 round2 round3 # assign keywords

result = 100/777
print(result) # 0.1287001287001287
print("The result was {}".format(result)) # The result was 0.1287001287001287
print("The result was {r}".format(r=result)) # The result was 0.1287001287001287
print("The result was {r:1.3f}".format(r=result)) # The result was 0.129 # {value[:width][.precision]f}
print("The result was {r:10.3f}".format(r=result)) # The result was      0.129
print("The result was {r:0.3f}".format(r=result)) # The result was 0.129
print("The result was {r:2.5f}".format(r=result)) # The result was 0.12870

name = 'Jose'
print(f'Hello, his name is {name}') # introduced in Python 3.6
name = "Sam"
age = 3
print(f"{name}'s age is {age}") # Sam's age is 3
```

### Lists in Python
Lists are ordered sequences that can hold a variety of object types. They use [] brackets and commas to separate objects in the list. [1, 2, 3, 4, 5]. Lists support indexing and slicing. Lists can be nested an also have a variety of useful methods than can be called off of them. 

```py
my_list = [1, 2, 3]
my_list = ["string", 100, 32.2] # can combine datatypes in list
print(len(my_list)) # 3 # return length of list

my_list = ['one', 'two', 'three']
print(my_list[0]) # 'one'
print(my_list[1:]) # ['two', 'three'] # slicing of list works like slicing of string 

another_list = ['four', 3.5]
new_list = my_list + another_list
print(new_list) # ['one', 'two', 'three', 'four', 3.5]

new_list[0] = 100 # you can mutate a list, unlike a string
print(new_list) # [100, 'two', 'three', 'four', 3.5]
new_list.append("six") # append a new element to end of list
print(new_list) # [100, 'two', 'three', 'four', 3.5, 'six']
new_list.pop() # remove an elem from the end of list
print(new_list) # [100, 'two', 'three', 'four', 3.5]
print(new_list.pop()) # 3.5 # pop() returns the val got popped out
print(new_list.pop(0)) # 100 # remove an elem of specified index
print(new_list.pop(-2)) # three # reverse index works for lists too

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]
new_list.sort() # sort the list in-place, so return nothing
print(new_list) # ['a', 'b', 'c', 'e', 'x']
print(sorted(new_list)) # ['a', 'b', 'c', 'e', 'x'] # this returns the sorted list
num_list.sort()
print(num_list) # [1, 3, 4, 8]
num_list.reverse()
print(num_list) # [8, 4, 3, 1]
```

### Dictionaries in Python
Dictionaries are unordered mappings (key-value pairs). They cannot be sorted. 
```py
my_dict = {'key1':'value1', 'key2':'value2'} # initialize a dict
print(my_dict) # {'key1': 'value1', 'key2': 'value2'}
print(my_dict['key2']) # value2 # retrieve a value based on its key

prices_lookup = {'apple':2.99, 'oranges':1.99, 'milk':5.80}
print(prices_lookup['apple']) # 2.99

prices_lookup = {'apple':2.99, 100:'test', 'milk':5.80} # no restriction on data types
print(prices_lookup[100]) # test

d = {'k1':123, 'k2':[0, 1, 2], 'k3':{'nestedKey':20}} # no restriction on data types, even nested dict or lists
print(d['k3']['nestedKey']) # 20
print(d['k2'][1]) # 1
d['k4'] = 100 # add key-value pair to dictionary
print(d) # {'k1': 123, 'k2': [0, 1, 2], 'k3': {'nestedKey': 20}, 'k4': 100}
d['k2'] = 'Hi' # update value of a key in a dict
print(d) # {'k1': 123, 'k2': 'Hi', 'k3': {'nestedKey': 20}, 'k4': 100}
print(d.keys()) # dict_keys(['k1', 'k2', 'k3', 'k4']) # show all keys of the dict
print(d.values()) # dict_values([123, 'Hi', {'nestedKey': 20}, 100]) # show all values of the dict
print(d.items()) # dict_items([('k1', 123), ('k2', 'Hi'), ('k3', {'nestedKey': 20}), ('k4', 100)]) # show all pairs in the form of tuples
```

### Tuples
Tuples are very similar to lists, but tuples are immutable. Once an element is assigned to a index position inside a tuple, it cannot be reassigned. 

When you pass objects in code, to make sure it doesn't get accidentally changes, use tuples. 
```py
t = (1, 2, 3)
mylist = [1, 2, 3]
print(type(t)) # <class 'tuple'>
print(type(mylist)) # <class 'list'>
print(len(t)) # 3 # return length of tuple

t = ('One', 2, [1, 2, 3]) # no restriction to data types
print(t[1]) # 2 # index a tuple
print(t[-1]) # [1, 2, 3] # can also use reverse index

t = ('a', 'a', 'b', 'z')
print(t.count('a')) # 2 # return how many times 'a' exists in the tuple
t.index('a') # 2 # return the index where 'a' appears for the first time in tuple
# t.index('hi') # will return error the value we look for does not exist

mylist[0] = 'New'
print(mylist) # ['New', 2, 3]
# t[0] = 'New' # expect an error, because of immutability
```

### Sets in Python
Unordered collections of unique elements. 
```py
myset = set() # initialize a set
myset.add(1) # add an element to this set
print(myset) # {1}
myset.add('Hi')
print(myset) # {1, 'Hi'}
myset.add(1) # re-adding existing elem will not cause err, will not dup either. 

mylist = [5, 'Hello', 1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 4]
myset = set(mylist) # cast a list to a set, could de-dup
print(myset) # {1, 2, 3, 4, 5, 'Hello'}
```

### Booleans
```py
print(True) # True
# print(true) # lowercase is not accepted
# Traceback (most recent call last):
#   File "/Users/lisa/Desktop/python/temp.py", line 175, in <module>
#     print(true)
# NameError: name 'true' is not defined
print(type(False)) # <class 'bool'>
print(1 > 2) # False # comparison operators returns a boolean
print(1 == 1) # True
b = None
print(b) # None
```

### I/O with basic files in Python
```py
myfile = open('myfile.txt') # if file not exist, will get error
myfile.read() # return a string of everything in the text file
myfile.read() # return nothing because cursor is at the end of the file
myfile.seek(0) # reset the cursor
myfile.read() # return a string of everything in the text file
myfile.seek(0)
myfile.readlines() # return a list with each line as a string
myfile.close() # close the file

# best practice, so you don't need to close this file by yourself
with open('myfile.txt') as f:
    contents = f.read()
print(contents) # a string of everything in the text file

with open('myfile.txt', mode = 'r') as f:
    contents = f.read()
# open function has different modes, default is r (read only)
# could also be: 
# w (write only, overwrite existing files or create new), 
# a (append only), 
# r+ (read and write), 
# w+ (write and read, overwrites existing file or create new)

with open('myfile.txt', mode = 'a') as f:
    f.write('this is the 4th line') # add a new line

with open('myfile.txt', mode = 'r') as f:
    print(f.read())

with open('newfile.txt', mode = 'w') as f:
    f.write("This is a new file\nLine2") # create a new file and write to it

with open('newfile.txt', mode = 'r') as f:
    print(f.read())
```
