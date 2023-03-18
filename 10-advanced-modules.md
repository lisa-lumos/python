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

## Math and Random

## Python Debugger

## Timeit

## Regular Expressions

## Unzipping and Zipping Modules






































