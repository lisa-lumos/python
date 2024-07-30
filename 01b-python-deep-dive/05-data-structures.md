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
## 5.4 Sets
## 5.5 Dictionaries
## 5.6 Looping Techniques
## 5.7 More on Conditions
## 5.8 Comparing Sequences and Other Types
