# 5. Data Structures
## 5.1 More on Lists
- list.append()
- list.extend(iterable)
- list.insert(idx, val)
- list.remove(val)
- list.pop([idx]): rmv the last elem, or the elem at idx
- list.clear()
- list.index(val, [startIdx, endIdx]): idx of 1st elem with this val, in idx range
- list.count(val)
- list.sort(*, key=None, reverse=False)
- list.reverse()
- list.copy(): shallow copy

### 5.1.1 Using Lists as Stacks
- list.append(val)
- list.pop()

### 5.1.2 Using Lists as Queues
Should not use list to achieve this, because add/rmv elem at the beginning of the list is slow. Should use deque module:
```py
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")     # Terry arrives
queue.append("Graham")    # Graham arrives
queue.popleft()           # Eric
queue.popleft()           # John
print(queue)
# deque(['Michael', 'Terry', 'Graham'])
```

### 5.1.3 List Comprehensions
```python
squares = []
for x in range(10):
    squares.append(x**2)

# it can be replaced by:
squares = list(map(lambda x: x**2, range(10)))
# or replaced by:
squares = [x**2 for x in range(10)]
```

### 5.1.4 Nested List Comprehensions
skipped 

## 5.2 The del statement
```py
a = [-1, 1, 66.25, 333, 333, 1234.5]

# Remove an item from a list given its index
del a[0] # [1, 66.25, 333, 333, 1234.5]

# rmv a slice from arr
del a[2:4] # [1, 66.25, 1234.5]

# rmv all vals
del a[:] # []

# delete entire variable
del a

```

## 5.3 Tuples and Sequences
A sequence data type, such as list/tuple/range. Tuples are immutable, but they can contain mutable objects such as lists: `v = ([1, 2, 3], [3, 2, 1])`. 

Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking/indexing, or even by attribute in the case of namedtuples. Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

The statement `t = 12345, 54321, 'hello!'` is an example of tuple packing - the values 12345, 54321 and 'hello!' are packed together in a tuple. The reverse operation is also possible: `x, y, z = t`.

Note that multiple assignment is really just a combination of tuple packing and sequence unpacking.

## 5.4 Sets
Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

```py
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # {'orange', 'banana', 'pear', 'apple'}
'orange' in basket # True
'crabgrass' in basket # False

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
a # {'a', 'r', 'b', 'c', 'd'}
a - b   # {'r', 'd', 'b'} in a but not in b
a | b   # {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'} in a or b, or both
a & b   # {'a', 'c'} in a and in b
a ^ b   # {'r', 'd', 'b', 'm', 'z', 'l'} in a or b, but not both

a = {x for x in 'abracadabra' if x not in 'abc'}
a # {'r', 'd'}
```

## 5.5 Dictionaries
## 5.6 Looping Techniques
## 5.7 More on Conditions
## 5.8 Comparing Sequences and Other Types
















