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

## OS module and Datetime

## Math and Random

## Python Debugger

## Timeit

## Regular Expressions

## Unzipping and Zipping Modules






































