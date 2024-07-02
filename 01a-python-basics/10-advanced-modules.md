# 10. Advanced Python Modules

## Collections
Specialized container types. 
```py
from collections import Counter
my_list = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 'abc', 'a', 'a']
c = Counter(my_list)
print(c) # Counter({3: 8, 1: 4, 2: 2, 'a': 2, 'abc': 1})
print(c.most_common()) # [(3, 8), (1, 4), (2, 2), ('a', 2), ('abc', 1)]. Orders by most common elements
print(c.most_common(2)) # [(3, 8), (1, 4)]. Orders by most common elements, list 2. 
print(list(c)) # [1, 2, 3, 'abc', 'a']. convert keys to a list

d = {'a':10} # this is a regular dictionary
print(d['a']) # 10. prints the value of key 'a'
print(d['wrong']) # returns error, because key does not exist

from collections import defaultdict
d = defaultdict(lambda: 0) # set default value of this dict
d['a'] = 10
print(d['a']) # 10
print(d['wrong']) # returns 0, because key does not exist, so use default value

my_tuple = (1, 2, 3)
print(my_tuple[0]) # 1

from collections import namedtuple
Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sammy = Dog(age=5, breed = 'Husky', name = 'Sam')
print(type(sammy)) # <class '__main__.Dog'>
print(sammy) # Dog(age=5, breed='Husky', name='Sam')
print(sammy.breed) # Husky
print(sammy[1]) # Husky

```

## OS module
Opening and reading files and folders. 
```py
f = open('practice.txt', 'w+')
f.write('This is a test string')
f.close()

import os
print(os.getcwd()) # returns current working directory
print(os.listdir()) # returns list of items as strings in cur dir
print(os.listdir('/Users/lisa/Desktop')) # returns list of items as strs in this dir
os.unlink('practice.txt') # permanently delete this file
os.rmdir('/Users/lisa/Desktop/my_folder') # permanently delete this folder
# recursively visit each nested dirs and files in this folder
for folder, sub_folders, files in os.walk('/Users/lisa/Desktop/my_folder'):
    print(f"Currently looking at {folder}\n")
    print('The subfolders are: ')
    for sub_folder in sub_folders:
        print(f'\t Subfolder: {sub_folder}')
    print('\nThe files are:')
    for f in files:
        print(f'\t File: {f}')

import shutil
shutil.move('practice.txt', '/Users/lisa/Desktop') # move this file to this folder
shutil.rmtree('/Users/lisa/Desktop/my_folder') # permanently delete all files and folders in this folder

import send2trash # pip install send2trash
send2trash.send2trash('practice.txt') # sends file to trash bin, instead of permanent removal
```

## Datetime
Useful when dealing with databases. 
```python
import datetime
my_time = datetime.time(2, 20) # hr, min, second, microsecond in 24 hr format
print(my_time.minute) # 20
print(my_time.hour) # 2
print(my_time) # 02:20:00

my_time = datetime.time(13, 20, 1, 20)
print(my_time) # 13:20:01.000020
print(type(my_time)) # <class 'datetime.time'>

today = datetime.date.today()
print(today) # 2023-03-20
print(today.year) # 2023
print(today.ctime()) # Mon Mar 20 00:00:00 2023

from datetime import datetime
my_datetime = datetime(2023, 3, 20, 15, 46, 12)
print(my_datetime) # 2023-03-20 15:46:12
my_datetime = my_datetime.replace(year=2024)
print(my_datetime) # 2024-03-20 15:46:12

from datetime import date
date1 = date(2023, 3, 20)
date2 = date(2024, 4, 20)
print(date2 - date1) # 397 days, 0:00:00
print(type(date2 - date1)) # <class 'datetime.timedelta'>

datetime1 = datetime(2023, 3, 20, 3)
datetime2 = datetime(2024, 4, 20, 4)
print(datetime2 - datetime1) # 397 days, 1:00:00
print(type(datetime2 - datetime1)) # <class 'datetime.timedelta'>
print((datetime2 - datetime1).total_seconds()) # 34304400.0
```

## Math and Random
```python
import math
value = 4.35
print(math.floor(value)) # 4
print(math.ceil(value)) # 5
print(round(4.5)) # 4 (round toward the even number if half way)
print(round(5.5)) # 6 (round toward the even number if half way)
print(math.pi) # 3.141592653589793
print(math.e) # 2.718281828459045
print(math.log(math.e)) # 1.0
print(math.log(100, 10)) # 2.0
print(math.inf) # inf
print(math.nan) # nan
print(math.sin(10)) # -0.5440211108893698
print(math.degrees(math.pi/2)) # 90.0
print(math.radians(180)) # 3.141592653589793

from math import pi
print(pi) # 3.141592653589793

import random
print(random.randint(0, 100)) # return an int within [0, 100]
random.seed(42) # if start with a fixed seed, will always use the same rand vals, no matter how many times you run it
print(random.randint(0, 100)) # 81
print(random.randint(0, 100)) # 14
print(random.randint(0, 100)) # 3

my_list = list(range(0, 20))
print(random.choice(my_list)) # randomly choose a val from my_list

print(random.choices(population=my_list, k=10)) # sample 10 elems with replacement
print(random.sample(population=my_list, k=10)) # sample 10 elems without replacement
random.shuffle(my_list) # shuffle the list in place
print(my_list)
print(random.uniform(a=0, b=100)) # choose a real number between a and b, each number have same likelihood of being chosen
print(random.gauss(mu=0, sigma=1)) # choose a real number between a and b, distribution is gauss distribution
```

## Python Debugger
Python comes with a built-in debugger tool that allows you to interactively explore variables within mid-operation of your Python code. A trace allow you to see the variables before the trace. 
```py
import pdb
x = [1, 2, 3]
y = 2
z = 3
result = y + z
pdb.set_trace() # set the trace before error line, press q to quit debugger
# command line:
# (Pdb) result
# 5
# (Pdb) y
# 2
# (Pdb) x
# [1, 2, 3]
result2 = x + y # should get an error, cannot add integer to a list
```
## Regular Expressions
Regular expressions (regex) can be used for general patterns in text data. For example, for a phone number `(555)-555-5555`, its regex pattern is `r"(\d\d\d)-\d\d\d-\d\d\d\d"`, or `r"(\d{3})-\d{3}-d{4}"`. 
```py
text = "The agent's phone number is 408-555-1234. Call soon!"
print('phone' in text) # returns True

import re
pattern = 'not in text'
print(re.search(pattern, text)) # None
pattern = 'phone'
print(re.search(pattern, text)) # <re.Match object; span=(12, 17), match='phone'>
match = re.search(pattern, text) # will only get the first match
print(match.span()) # (12, 17)
print(match.start()) # 12
print(match.end()) # 17

text = "phone once, phone twice"
matches = re.findall('phone', text) # find all patterns in a string
print(matches) # ['phone', 'phone']
for match in re.finditer('phone', text): # find each match
    print(match)
# returns: 
# <re.Match object; span=(0, 5), match='phone'>
# <re.Match object; span=(12, 17), match='phone'>

# character identifiers: 
# \d    => a digit
# \w    => a letter, or a digit, or an underscore
# \s    => a white space
# \D    => not a digit
# \W    => not a letter, nor a digit, not an underscore
# \S    => not a white space

# quantifiers that decorates the one character identifier or char before it:
# +     => occurs one or more times, e.g.: "Version \w-\w+" => "Version A-b1_1"
# {3}   => occurs exactly 3 times, e.g.: "\D{3}" => "abc"
# {2,4} => occurs 2 to 4 times, e.g.: "\d{2,4}" => "123"
# {3,}  => occurs >=3 times, e.g.: "\w{3,}" => "123_abc"
# *     => occurs >= 0 times, e.g.: "A*B*C*" => "AAACC"
# ?     => occurs 0 or 1 times, e.g.: "plurals?" => "plural"

text = 'My phone number is 123-456-7890'
phone = re.search('123-456-7890', text)
print(phone) # <re.Match object; span=(19, 31), match='123-456-7890'>
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text) # need r before string pattern
print(phone) # <re.Match object; span=(19, 31), match='123-456-7890'>
print(phone.group()) # 123-456-7890

phone = re.search(r'\d{3}-\d{3}-\d{4}', text) # need r before string pattern
print(phone) # <re.Match object; span=(19, 31), match='123-456-7890'>
print(phone.group()) # 123-456-7890

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # '()-()-()' groups 3 regex
results = re.search(phone_pattern, text)
print(results.group()) # 123-456-7890
# access each of the 3 groups, idx starts from 1: 
print(results.group(1)) # 123
print(results.group(2)) # 456
print(results.group(3)) # 7890
```

## Timeit
Can be used to time your code's performance. 
```py
def func_one(n):
    return [str(num) for num in range(n)]

print(func_one(10)) # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def func_two(n):
    return list(map(str, range(n)))

print(func_two(10)) # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# method 1: use time difference. Problem: precision is not good enough for fast code
import time
start_time =  time.time()
result = func_one(1000000)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time) # 0.06716489791870117 # unit is in seconds

start_time =  time.time()
result = func_two(1000000)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time) # 0.06970787048339844 

# method 2: use the timeit module. 
import timeit
statement = '''
func_one(100)
''' # the statement to test performance, in the form of a string
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
''' # the function used in the statement
avg_time = timeit.timeit(statement, setup, number=1000000)
print(avg_time) # 5.778604458086193
statement = '''
func_two(100)
''' # the statement to test performance, in the form of a string
setup = '''
def func_two(n):
    return list(map(str, range(n)))
''' # the function used in the statement
avg_time = timeit.timeit(statement, setup, number=1000000)
print(avg_time) # 5.254787957994267
```

## Unzipping and Zipping Modules
```py
f = open('file1.txt', 'w+')
f.write('one file')
f.close()

f = open('file2.txt', 'w+')
f.write('two file')
f.close()

import zipfile # this has to put file into zip one by one
comp_file = zipfile.ZipFile('comp_file.zip', 'w') # write items to this zip file
comp_file.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
zip_obj.extractall('extracted_content') # unzip to this folder

import shutil # this can do a dir into a zip all at once
dir_to_zip = '/mypath/extracted_content'
output_filename = 'example'
shutil.make_archive(output_filename, 'zip', dir_to_zip) # will zip source dir into example.zip file 
shutil.unpack_archive('example.zip', 'folder_to_unzip', 'zip') # unzip to this folder
```



































