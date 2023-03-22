# def create_cubes_v1(n): # generates the list in memory as a whole
#     result = []
#     for x in range(n):
#         result.append(x**3)
#     return result

# print(create_cubes_v1(10)) # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# def create_cubes_v2(n): # the memory efficient way
#     for x in range(n):
#         yield x**3

# for x in create_cubes_v2(10):
#     print(x)

# print(list(create_cubes_v2(10)))  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# def gen_fib(n):
#     a = 1
#     b = 1
#     for i in range(n):
#         yield a
#         a, b = b, a+b

# print(list(gen_fib(10))) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# def simple_gen():
#     for x in range(3):
#         yield x

# for x in simple_gen(): # 0 1 2
#     print(x)

# g = simple_gen()
# print(next(g)) # 0
# print(next(g)) # 1
# print(next(g)) # 2
# # print(next(g)) # StopIteration Error. Note we don't get this error in "for loop" because it automatically catches the error. 

# s = 'hello'
# for letter in s: # h e l l o
#     print(letter)

# # next(s) # TypeError: 'str' is not an iterator
# s_iter =  iter(s)
# print(next(s_iter)) # h
# print(next(s_iter)) # e

# from collections import Counter
# my_list = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 'abc', 'a', 'a']
# c = Counter(my_list)
# print(c) # Counter({3: 8, 1: 4, 2: 2, 'a': 2, 'abc': 1})
# print(c.most_common()) # [(3, 8), (1, 4), (2, 2), ('a', 2), ('abc', 1)]. Orders by most common elements
# print(c.most_common(2)) # [(3, 8), (1, 4)]. Orders by most common elements, list 2. 
# print(list(c)) # [1, 2, 3, 'abc', 'a']. convert keys to a list


# d = {'a':10} # this is a regular dictionary
# print(d['a']) # 10. prints the value of key 'a'
# print(d['wrong']) # returns error, because key does not exist

# from collections import defaultdict
# d = defaultdict(lambda: 0) # set default value of this dict
# d['a'] = 10
# print(d['a']) # 10
# print(d['wrong']) # returns 0, because key does not exist, so use default value

# my_tuple = (1, 2, 3)
# print(my_tuple[0]) # 1

# from collections import namedtuple
# Dog = namedtuple('Dog', ['age', 'breed', 'name'])
# sammy = Dog(age=5, breed = 'Husky', name = 'Sam')
# print(type(sammy)) # <class '__main__.Dog'>
# print(sammy) # Dog(age=5, breed='Husky', name='Sam')
# print(sammy.breed) # Husky
# print(sammy[1]) # Husky

# f = open('practice.txt', 'w+')
# f.write('This is a test string')
# f.close()

# import os
# print(os.getcwd()) # returns current working directory
# print(os.listdir()) # returns list of items as strings in cur dir
# print(os.listdir('/Users/lisa/Desktop')) # returns list of items as strs in this dir
# os.unlink('practice.txt') # delete this file
# os.rmdir('/Users/lisa/Desktop/my_folder') # delete this folder

# import shutil
# shutil.move('practice.txt', '/Users/lisa/Desktop') # move this file to this folder
# shutil.rmtree('/Users/lisa/Desktop/my_folder') # delete all files and folders in this folder

# import send2trash # pip install send2trash
# send2trash.send2trash('practice.txt') # sends file to trash bin, instead of permanent removal

# # recursively visit each nested dirs and files in this folder
# for folder, sub_folders, files in os.walk('/Users/lisa/Desktop/my_folder'):
#     print(f"Currently looking at {folder}\n")
#     print('The subfolders are: ')
#     for sub_folder in sub_folders:
#         print(f'\t Subfolder: {sub_folder}')
#     print('\nThe files are:')
#     for f in files:
#         print(f'\t File: {f}')

# import datetime
# my_time = datetime.time(2, 20) # hr, min, second, microsecond in 24 hr format
# print(my_time.minute) # 20
# print(my_time.hour) # 2
# print(my_time) # 02:20:00

# my_time = datetime.time(13, 20, 1, 20)
# print(my_time) # 13:20:01.000020
# print(type(my_time)) # <class 'datetime.time'>

# today = datetime.date.today()
# print(today) # 2023-03-20
# print(today.year) # 2023
# print(today.ctime()) # Mon Mar 20 00:00:00 2023

# from datetime import datetime
# my_datetime = datetime(2023, 3, 20, 15, 46, 12)
# print(my_datetime) # 2023-03-20 15:46:12
# my_datetime = my_datetime.replace(year=2024)
# print(my_datetime) # 2024-03-20 15:46:12

# from datetime import date
# date1 = date(2023, 3, 20)
# date2 = date(2024, 4, 20)
# print(date2 - date1) # 397 days, 0:00:00
# print(type(date2 - date1)) # <class 'datetime.timedelta'>

# datetime1 = datetime(2023, 3, 20, 3)
# datetime2 = datetime(2024, 4, 20, 4)
# print(datetime2 - datetime1) # 397 days, 1:00:00
# print(type(datetime2 - datetime1)) # <class 'datetime.timedelta'>
# print((datetime2 - datetime1).total_seconds()) # 34304400.0

# import math
# value = 4.35
# print(math.floor(value)) # 4
# print(math.ceil(value)) # 5
# print(round(4.5)) # 4 (round toward the even number if half way)
# print(round(5.5)) # 6 (round toward the even number if half way)
# print(math.pi) # 3.141592653589793
# print(math.e) # 2.718281828459045
# print(math.log(math.e)) # 1.0
# print(math.log(100, 10)) # 2.0
# print(math.inf) # inf
# print(math.nan) # nan
# print(math.sin(10)) # -0.5440211108893698
# print(math.degrees(math.pi/2)) # 90.0
# print(math.radians(180)) # 3.141592653589793

# from math import pi
# print(pi) # 3.141592653589793

# import random
# print(random.randint(0, 100)) # return an int within [0, 100]
# random.seed(42) # if start with a fixed seed, will always use the same rand vals, no matter how many times you run it
# print(random.randint(0, 100)) # 81
# print(random.randint(0, 100)) # 14
# print(random.randint(0, 100)) # 3

# my_list = list(range(0, 20))
# print(random.choice(my_list)) # randomly choose a val from my_list

# print(random.choices(population=my_list, k=10)) # sample 10 elems with replacement
# print(random.sample(population=my_list, k=10)) # sample 10 elems without replacement
# random.shuffle(my_list) # shuffle the list in place
# print(my_list)
# print(random.uniform(a=0, b=100)) # choose a real number between a and b, each number have same likelihood of being chosen
# print(random.gauss(mu=0, sigma=1)) # choose a real number between a and b, distribution is gauss distribution

# import pdb
# x = [1, 2, 3]
# y = 2
# z = 3
# result = y + z
# pdb.set_trace() # set the trace before error line, press q to quit debugger
# # command line:
# # (Pdb) result
# # 5
# # (Pdb) y
# # 2
# # (Pdb) x
# # [1, 2, 3]
# result2 = x + y # should get an error, cannot add integer to a list

# text = "The agent's phone number is 408-555-1234. Call soon!"
# print('phone' in text) # returns True

# import re
# pattern = 'not in text'
# print(re.search(pattern, text)) # None
# pattern = 'phone'
# print(re.search(pattern, text)) # <re.Match object; span=(12, 17), match='phone'>
# match = re.search(pattern, text) # will only get the first match
# print(match.span()) # (12, 17)
# print(match.start()) # 12
# print(match.end()) # 17

# text = "phone once, phone twice"
# matches = re.findall('phone', text) # find all patterns in a string
# print(matches) # ['phone', 'phone']
# for match in re.finditer('phone', text): # find each match
#     print(match)
# # returns: 
# # <re.Match object; span=(0, 5), match='phone'>
# # <re.Match object; span=(12, 17), match='phone'>

# import re
# text = 'My phone number is 123-456-7890'
# phone = re.search('123-456-7890', text)
# print(phone) # <re.Match object; span=(19, 31), match='123-456-7890'>
# phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text) # need r before string pattern
# print(phone) # <re.Match object; span=(19, 31), match='123-456-7890'>
# print(phone.group()) # 123-456-7890

# phone = re.search(r'\d{3}-\d{3}-\d{4}', text) # need r before string pattern
# print(phone) # <re.Match object; span=(19, 31), match='123-456-7890'>
# print(phone.group()) # 123-456-7890

# phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # '()-()-()' groups 3 regex
# results = re.search(phone_pattern, text)
# print(results.group()) # 123-456-7890
# # access each of the 3 groups, idx starts from 1: 
# print(results.group(1)) # 123
# print(results.group(2)) # 456
# print(results.group(3)) # 7890






