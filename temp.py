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






















