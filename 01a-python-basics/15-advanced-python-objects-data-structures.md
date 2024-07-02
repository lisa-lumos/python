# 15. Advanced Python objects and data structures
```py
print(hex(12)) # 0xc
print(bin(3)) # 0b11
print(pow(2, 3)) # 8
print(abs(-2)) # 2
print(round(3.1)) # 3
print(round(3.141592, 2)) # 3.14

s = 'hello world'
print(s.capitalize()) # Hello world # capitalizes the first word in the str
print(s.upper()) # HELLO WORLD
print(s.lower()) # hello world
print(s.count('o')) # 2 # count num of letter o in the str
print(s.find('o')) # 4 # find the first idx of o
print(s.center(20, '-')) # ----hello world----- # center the string between dashes, total length is 20
s = 'hello'
print(s.isalnum()) # True # checks if all chars in str are alpha-numeric 
print(s.isalpha()) # True # checks if all chars in str are alphabetic 
print(s.islower()) # True # checks if all chars in str are lowercase
print(s.isupper()) # False # checks if all chars in str are uppercase
print(s.isspace()) # False # checks if all chars in str are whitespace
print(s.istitle()) # False # checks if each word start with an upper case letter
print(s.endswith('o')) # True
print(s.split('e')) # ['h', 'llo'] # separate at every occurrence
print(s.partition('l')) # ('he', 'l', 'lo')

s = set()
s.add(1)
s.add(2)
s.add(2)
print(s) # {1, 2}
s.clear()
print(s) # set()
s = {1, 2, 3}
sc = s.copy() # copy is a deep copy
print(sc) # {1, 2, 3}
s.add(4)
print(sc) # {1, 2, 3}
print(s.difference(sc)) # {4} # shows the difference between two sets
s.difference_update(sc) # {4} # remove from s the duplicates between s and sc
print(s)
s = {1, 2, 3, 4}
s.discard(2)
print(s) # {1, 3, 4} 
s1 = {1, 2, 3}
s2 = {1, 2, 4}
print(s1.intersection(s2)) # {1, 2}
s1.intersection_update(s2) # update s1 as the intersection
print(s1) # {1, 2}
s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}
print(s1.isdisjoint(s2)) # False # if have no common elems
print(s3.isdisjoint(s2)) # True
print(s1.issubset(s2)) # True
print(s2.issuperset(s1)) # True
print(s1.union(s2)) # {1, 2, 4}
s1.update(s2) # s1 becomes the union of both

d = {'k1': 1, 'k2': 2}
print({x:x**2 for x in range(10)}) # using list comprehension to create a dict
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print({k:v**2 for k,v in zip(['a', 'b', 'c'], range(10))})
# {'a': 0, 'b': 1, 'c': 4}
for pair in d.items():
    print(pair)
# ('k1', 1)
# ('k2', 2)
for k in d.keys():
    print(k)
# k1
# k2
for v in d.values():
    print(v)
# 1
# 2

l = [1, 2, 3]
l.append(4)
print(l) # [1, 2, 3, 4]
print(l.count(3)) # 1 # count num of occurrences of 3
l.append([4, 5])
print(l) # [1, 2, 3, 4, [4, 5]]
l.extend([6, 7]) # append one by one from the iterable
print(l) # [1, 2, 3, 4, [4, 5], 6, 7]
print(l.index(7)) # 6 # will get error if val not exist
l.insert(2, 'inserted') # insert at idx 2
print(l) # [1, 2, 'inserted', 3, 4, [4, 5], 6, 7]
print(l.pop()) # 7 # pop last elem out of the list
print(l) # [1, 2, 'inserted', 3, 4, [4, 5], 6]
print(l.pop(0)) # 1 # pop the indexed elem out of the list
print(l) # [2, 'inserted', 3, 4, [4, 5], 6]
l.remove('inserted') # remove the first occurrence of 'inserted'
print(l) # [2, 3, 4, [4, 5], 6]
l = [1, 2, 3]
l.reverse()
print(l) # [3, 2, 1]
l.sort()
print(l) # [1, 2, 3]
```


























