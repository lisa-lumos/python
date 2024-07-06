# 3. An Informal Introduction to Python
## 3.1 Using Python as a Calculator
### 3.1.1 Numbers
```py
>>> 17 / 3  # classic division returns a float
5.666666666666667

>>> 17 // 3  # floor division discards the fractional part
5

>>> 5 ** 2  # 5 squared
25
```

### 3.1.2 Text
If you don't want characters prefaced by `\` to be interpreted as special characters, you can use raw strings by adding an `r` before the first quote:
```py
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```

String literals can span multiple lines. One way is using triple-quotes: `"""..."""` or `'''...'''`. End of lines are automatically included in the string, but it's possible to prevent this by adding a `\` at the end of the line. e.g.:
```py
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to
```

Python strings cannot be changed - they are immutable. Therefore, assigning to an indexed position in the string results in an error. 

### 3.1.3 Lists
Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content.

All slice operations return a new list containing the requested elements. 

The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):
- A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
- A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

Assignment to slices is also possible, and this can even change the size of the list, or clear it entirely. 

## 3.2 First Steps Towards Programming
skip.
