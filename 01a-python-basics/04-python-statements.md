# Python Statements
## if elif and else
```py
hungry = False
if hungry: 
  print('Feed dog!')
else:
  print('Dog not hungry. ')

loc = 'Bank'
if loc == 'Auto Shop':
  print('loc is Auto Shot')
elif loc == 'Bank':
  print('loc is Bank')
else:
  print('I have no idea')
```

## for loops
```py
mylist = [1, 2, 3, 4]
for num in mylist:
  print(num)
# 1
# 2
# 3
# 4

for num in mylist:
  if num % 2 == 0: # check for even
    print(num)
  else:
    print(f'Odd Number: {num}')
# Odd Number: 1
# 2
# Odd Number: 3
# 4

mystr = 'Hello World'
for letter in mystr:
  print(letter) # print each char on each line

for _ in 'Hi': # use low dash if don't need the var
  print('Cool')
# Cool
# Cool

tup = (1, 2, 3)
for item in tup: # can iterate over tuple
  print(item)

mylist = [(1, 2), (3, 4), (5, 6)]
for item in mylist:
  print(item)
# (1, 2)
# (3, 4)
# (5, 6)

for (a, b) in mylist: # tuple unpacking
  print(a)
  print(b)
# 1
# 2
# 3
# 4
# 5
# 6

for a, b in mylist: # tuple unpacking
  print(b)
# 2
# 4
# 6

d = {'k1':1, 'k2':2, 'k3':3}
for item in d: # by default, only loop over keys in a dict
  print(item)
# k1
# k2
# k3
for item in d.items(): # output key-value pair
  print(item)
# ('k1', 1)
# ('k2', 2)
# ('k3', 3)
for key, val in d.items(): # output key-value pair using tuple unpacking
  print(val)
# 1
# 2
# 3
for val in d.values(): # output only values
  print(val)
# 1
# 2
# 3
```

## while loops
```py
 = 0
while x < 5:
    print(f'The cur val of x is {x}')
    x += 1
else:
    print('x is not less than 5')
# The cur val of x is 0
# The cur val of x is 1
# The cur val of x is 2
# The cur val of x is 3
# The cur val of x is 4
# x is not less than 5
```

## useful operators in Python
```py
x = [1, 2, 3]
for item in x:
    # if nothing in this part, then will have error
    pass # this does nothing, but help avoid syntax error
    # it can act as a place holder for your function content

mystring = 'sammy'
for letter in mystring:
    if letter == 'a':
        continue # Python has continue statement
    print(letter)
# s
# m
# m
# y

mystring = 'sammy'
for letter in mystring:
    if letter == 'a':
        break # Python has break statement
    print(letter)
# s

for num in range(10): # means range [0, 10)
    print(num)

for num in range(3, 10, 2): # means range [3, 10), step of 2
    print(num)

print(list(range(0, 11, 2))) # [0, 2, 4, 6, 8, 10] # cast a range to a list

idx = 0
for letter in 'abcde':
    print('at idx {} the letter is {}'.format(idx, letter))
    idx += 1
# at idx 0 the letter is a
# at idx 1 the letter is b
# at idx 2 the letter is c
# at idx 3 the letter is d
# at idx 4 the letter is e

word = 'abcde'
for item in enumerate(word): # use enumerate to do same as above cell
    print(item) # each item is a tuple
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')

# now add tuple unpacking
word = 'abcde'
for idx, letter in enumerate(word): 
    print(idx, letter) 
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e

mylist1 = [1, 2, 3, 4, 5]
mylist2 = ['a', 'b', 'c']
mylist3 = ['h', 'i']
for item in zip(mylist1, mylist2): # zip function produces a "collection" of tuples
    print(item)
# (1, 'a')
# (2, 'b')
# (3, 'c')
for item in zip(mylist1, mylist2, mylist3): # zip() takes many inputs, output length is same with the shortest one
    print(item)
# (1, 'a', 'h')
# (2, 'b', 'i')

print(list(zip(mylist1, mylist2))) # [(1, 'a'), (2, 'b'), (3, 'c')] # cast the output of zip() to a list
print(zip(mylist1, mylist2, mylist3)) # <zip object at 0x7fb8a01d6240> # produces nothing if you do not cast it

print('x' in [1, 2, 3]) # False # the "in" operator
print('x' in ['x', 'y', 'z']) # True # "in" works for a list
print('abc' in 'xabcdef') # True # "in" also works for string
print('mykey' in {'key1': 100, 'key2': 200})  # False # "in" works in dict
print('mykey' in {'mykey': 100, 'key2': 200}) # True

d = {'mykey': 100, 'key2': 200}
print(100 in d.values()) # True

mylist = [1, 3, 4, 5, 5]
print(min(mylist)) # 1 # return min val in a list
print(max(mylist)) # 5

from random import shuffle # import a library
mylist = [1, 2, 3, 4, 5, 6, 7, 8]
shuffle(mylist) # shuffle the list in place
print(mylist) # [8, 1, 6, 3, 4, 2, 5, 7]

from random import randint
print(randint(0, 100)) # 96 # return a random integer in range [0, 100]

my_val = input('What is your name?') # ask for user input, get a string
print(my_val) # Lisa
```

## List Comprehensions
Quickly create a list with Python
```py
mystring = 'hello'
mylist = []
for letter in mystring: # The old way of creating a list
    mylist.append(letter)
print(mylist) # ['h', 'e', 'l', 'l', 'o']

mylist = [letter for letter in mystring] # using list comprehension
print(mylist) # ['h', 'e', 'l', 'l', 'o']

mylist = [num for num in range(0, 11)] # using list comprehension
print(mylist) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mylist = [num**2 for num in range(0, 11)] # using list comprehension
print(mylist) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

mylist = [num for num in range(0, 11) if num%2 == 0] # using list comprehension, only return even numbers
print(mylist) # [0, 2, 4, 6, 8, 10]

mylist = [num**2 for num in range(0, 11) if num%2 == 0] # using list comprehension, only return even numbers then square
print(mylist) # [0, 4, 16, 36, 64, 100]

celsius = [0, 10, 20, 35.1]
fahrenheit = [(9/5*temp + 32) for temp in celsius] # more complex calcs
print(fahrenheit) # [32.0, 50.0, 68.0, 95.18]

results = [x if x%2==0 else 'Odd' for x in range(0, 11)] # not recommended, hard to read
print(results) # [0, 'Odd', 2, 'Odd', 4, 'Odd', 6, 'Odd', 8, 'Odd', 10]

mylist = []
for x in [2, 4, 6]:
    for y in [1, 10, 100]:
        mylist.append(x*y) 
print(mylist) # [2, 20, 200, 4, 40, 400, 6, 60, 600]

mylist = [x*y for x in [2, 4, 6] for y in [1, 10, 100]]
print(mylist) # [2, 20, 200, 4, 40, 400, 6, 60, 600]
```

