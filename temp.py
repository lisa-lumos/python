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

# import re
# print(re.search(r'cat', 'The cat is here')) # <re.Match object; span=(4, 7), match='cat'>
# print(re.search(r'cat|dog', 'The dog is here')) # <re.Match object; span=(4, 7), match='dog'> # the pipe operator, for "or" operation
# print(re.findall(r'at', 'The cat in the hat sat there.')) # ['at', 'at', 'at']
# print(re.findall(r'.at', 'The cat in the hat sat there.')) # ['cat', 'hat', 'sat'] # wildcard operator
# print(re.findall(r'...at', 'The cat in the hat sat there.')) # ['e cat', 'e hat'] # wildcard operator
# print(re.findall(r'^\d', '2 is a number')) # ['2'] # search for the number that starts the string, ^ means starts with
# print(re.findall(r'\d$', '2 is a number, so is 3')) # ['3'] # search for the number that ends the string, $ means ends with
# phrase = 'there are 3 numbers 34 inside 5 this sentence'
# pattern = r'[^\d]+' # exclude single/continuous digits, [] are often used for excludes
# print(re.findall(pattern, phrase)) # ['there are ', ' numbers ', ' inside ', ' this sentence']

# phrase = 'This is a string! But it has punctuation. We need to remove them. '
# print(re.findall(r'[^!.?]+', phrase)) # ['This is a string', ' But it has punctuation', ' We need to remove them', ' ']
# words = re.findall(r'[^!.? ]+', phrase) # ['This', 'is', 'a', 'string', 'But', 'it', 'has', 'punctuation', 'We', 'need', 'to', 'remove', 'them'] # also removes spaces, and return a list
# print(words) 
# print(' '.join(words)) # This is a string But it has punctuation We need to remove them

# text = 'Only find the dash-words in this sentence. But you do not know how long-ish they are. '
# pattern = r'[\w]+'
# print(re.findall(pattern, text)) # ['Only', 'find', 'the', 'dash', 'words', 'in', 'this', 'sentence', 'But', 'you', 'do', 'not', 'know', 'how', 'long', 'ish', 'they', 'are'] # return all alphanumerics. 
# pattern = r'[\w]+-[\w]+' # alphanumerics-alphanumerics
# print(re.findall(pattern, text)) # ['dash-words', 'long-ish']

# text = 'Hello, would you like some catfish? or catnap? or caterpillar?'
# pattern = r'cat(fish|nap|claw)' # use () for a group of or operations
# print(re.search(pattern, text)) # <re.Match object; span=(27, 34), match='catfish'>

# def func_one(n):
#     return [str(num) for num in range(n)]

# print(func_one(10)) # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# def func_two(n):
#     return list(map(str, range(n)))

# print(func_two(10)) # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# # method 1: use time difference. Problem: precision is not good enough for fast code
# import time
# start_time =  time.time()
# result = func_one(1000000)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(elapsed_time) # 0.06716489791870117 # unit is in seconds

# start_time =  time.time()
# result = func_two(1000000)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(elapsed_time) # 0.06970787048339844 

# # method 2: use the timeit module. 
# import timeit
# statement = '''
# func_one(100)
# ''' # the statement to test performance, in the form of a string
# setup = '''
# def func_one(n):
#     return [str(num) for num in range(n)]
# ''' # the function used in the statement
# avg_time = timeit.timeit(statement, setup, number=1000000)
# print(avg_time) # 5.778604458086193
# statement = '''
# func_two(100)
# ''' # the statement to test performance, in the form of a string
# setup = '''
# def func_two(n):
#     return list(map(str, range(n)))
# ''' # the function used in the statement
# avg_time = timeit.timeit(statement, setup, number=1000000)
# print(avg_time) # 5.254787957994267

# f = open('file1.txt', 'w+')
# f.write('one file')
# f.close()

# f = open('file2.txt', 'w+')
# f.write('two file')
# f.close()

# import zipfile # this has to put file into zip one by one
# comp_file = zipfile.ZipFile('comp_file.zip', 'w') # write items to this zip file
# comp_file.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)
# comp_file.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)
# comp_file.close()

# zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
# zip_obj.extractall('extracted_content') # unzip to this folder

# import shutil # this can do a dir into a zip all at once
# dir_to_zip = '/mypath/extracted_content'
# output_filename = 'example'
# shutil.make_archive(output_filename, 'zip', dir_to_zip) # will zip source dir into example.zip file 
# shutil.unpack_archive('example.zip', 'folder_to_unzip', 'zip') # unzip to this folder

# import requests
# result = requests.get("http://www.example.com")
# print(type(result)) # requests.models.Response
# print(result.text) # return the html document contents # '<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n    <meta charset="utf-8" />\n    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\n    <style type="text/css">\n    body {\n        background-color: #f0f0f2;\n        margin: 0;\n        padding: 0;\n        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;\n        \n    }\n    div {\n        width: 600px;\n        margin: 5em auto;\n        padding: 2em;\n        background-color: #fdfdff;\n        border-radius: 0.5em;\n        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);\n    }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n    }\n    @media (max-width: 700px) {\n        div {\n            margin: 0 auto;\n            width: auto;\n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n    <h1>Example Domain</h1>\n    <p>This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.</p>\n    <p><a href="https://www.iana.org/domains/example">More information...</a></p>\n</div>\n</body>\n</html>\n'

# import bs4 # beautifulSoup library can obtain info from html string
# soup = bs4.BeautifulSoup(result.text, "lxml") # lxml is the engine to use to parse the html text
# print(soup) # # makes it easy to read, in indented format, with multiple lines
# soup.select('title') # grab things from the html document, based on tag name, returns a list # [<title>Example Domain</title>]
# soup.select('p') # 
# # [<p>This domain is for use in illustrative examples in documents. You may use this
# #      domain in literature without prior coordination or asking for permission.</p>,
# #  <p><a href="https://www.iana.org/domains/example">More information...</a></p>]
# soup.select('title')[0].getText() # getText() method removes the tag name in the specified bs4 object element # 'Example Domain'
# soup.select('div') # returns all elements with a 'div' tag
# soup.select('#my_id') # returns elements with this id
# soup.select('.my_class') # returns elements with this class
# soup.select('div span') # returns elements with tag name 'span' within a 'div' element
# soup.select('div > span') # returns elements with tag name 'span' directly within a div element, with nothing in between

# import requests
# import bs4
# res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
# soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup.select('div .vector-toc-text'))
# # Output exceeds the size limit. Open the full output data in a text editor
# # [<div class="vector-toc-text">(Top)</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">1</span>Early life and education</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">2</span>Career</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">2.1</span>World War II</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">2.2</span>UNIVAC</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">2.3</span>COBOL</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">2.4</span>Standards</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">3</span>Retirement</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">4</span>Post-retirement</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">5</span>Anecdotes</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">6</span>Death</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">7</span>Dates of rank</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">8</span>Awards and honors</div>,
# # ...
# #  <span class="vector-toc-numb">13</span>References</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">14</span>Further reading</div>,
# #  <div class="vector-toc-text">
# #  <span class="vector-toc-numb">15</span>External links</div>]
# print(soup.select('div .vector-toc-text')[1].text) # '\n1Early life and education'
# for item in soup.select('div .vector-toc-text'):
#     print(item.getText())
# # Output exceeds the size limit. Open the full output data in a text editor
# # (Top)

# # 1Early life and education

# # 2Career

# # 2.1World War II

# # 2.2UNIVAC

# # 2.3COBOL

# # 2.4Standards

# # 3Retirement

# # 4Post-retirement

# # 5Anecdotes

# # 6Death

# # 7Dates of rank

# # 8Awards and honors
# # ...

# # 14Further reading

# # 15External links


# import requests
# import bs4
# res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
# soup = bs4.BeautifulSoup(res.text, 'lxml')
# list_of_img_tags = soup.select('img')
# # print(list_of_img_tags[3]) # shows an image tag
# list_of_img_tags = soup.select('.thumbimage')
# # print(list_of_img_tags)
# link1_text = list_of_img_tags[0]['src']
# print(link1_text)
# img_link = requests.get('https:' + link1_text)
# print('https:' + link1_text)
# f = open('image.jpg', 'wb') # write binary for this image
# f.write(img_link.content)
# f.close()

# from PIL import Image # pip install pillow
# image_file = Image.open('cat.jpg')
# # image_file.show() # this opens the image to view
# print(image_file.size) # (481, 480) # print out the size of the image
# print(image_file.filename) # cat.jpg 
# print(image_file.format_description) # JPEG (ISO 10918)
# image_file.crop((0, 0, 100, 200)).show() # origin is top left corner. start from origin, width = 100px, and hight = 200px. returns the cropped file. 
# cropped_file = image_file.crop((50, 50, 100, 200))
# image_file.paste(im=cropped_file, box=(0, 0)) # put cropped_file at origin of the image_file, modify image_file in-place
# image_file.show()
# image_file.resize((2000, 300)).show() # stretch this file, return a stretched file
# image_file.rotate(90).show() # rotate this image by 90 deg, return a new file

# red = Image.open('red.jpg') # opens a red image
# blue = Image.open('blue.jpg') # opens a blue image
# blue.putalpha(128) # changes the transparency of this image in place. 0 is complete transparent, 255 is not transparent at all
# red.putalpha(128) 
# blue.paste(im=red, box=(0, 0)) # paste red on top of blue, now blue is a purple image
# blue.save('purple.png') # save this image as file, overwrite if already exists

# import csv
# data = open('example.csv', encoding='utf-8')
# csv_data = csv.reader(data)
# data_lines = list(csv_data) # a col list of row val lists
# for line in data_lines[:5]:
#     print(line) # print the first 5 rows
# # write to a csv file: 
# output_file = open('saved-file.csv', mode='w', newline='')
# csv_writer = csv.writer(output_file, delimiter=',')
# csv_writer.writerow(['a', 'b', 'c']) # write a single row
# csv_writer.writerows(['1', '2', '3'], ['4', '5', '6']) # write multiple rows
# output_file.close()
# f = open('saved-file.csv', mode='a', newline='') # append to this file
# csv_writer = csv.writer(f)
# csv_writer.writerow(['a2', 'b2', 'c2']) 
# f.close()

# import PyPDF2 # pip install PyPDF2
# f = open('test.pdf', 'rb')
# pdf_reader = PyPDF2.PdfFileReader(f)
# print(pdf_reader.numPages) # show num of pages in the pdf file
# page0 = pdf_reader.getPage(0) # grab the first page
# page0_text = page0.extractText() # extract text as string
# print(page0_text)
# f.close()

# # write to a new pdf file
# f = open('test.pdf', 'rb')
# pdf_reader = PyPDF2.PdfFileReader(f)
# page0 = pdf_reader.getPage(0) 
# pdf_writer = PyPDF2.PdfFileWriter()
# pdf_writer.addPage(page0)
# f_out = open('newfile.pdf', 'wb')
# pdf_writer.write(f_out)
# f_out.close()














