# 9. Classes
Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

Python classes provide all the standard features of Object Oriented Programming: - the class inheritance mechanism allows multiple base classes
- a derived class can override any methods of its base class or classes
- a method can call the method of a base class with the same name
- objects can contain arbitrary amounts and kinds of data

## 9.1 A Word About Names and Objects
skipped.

## 9.2 Python Scopes and Namespaces
Strictly speaking, references to names in modules are attribute refs: in the expression `module_name.func_name`, `module_name` is a module object and `func_name` is an attribute of it.

Attributes may be read-only or writable. If writable, assignment to attributes is possible. Module attributes are writable, e.g. `module_name.the_answer = 42`. Writable attributes may also be deleted with `del`, e.g., `del module_name.the_answer` will remove the attribute the_answer from the object named by `module_name`.

The statements executed by the top-level invocation of the interpreter, either read from a script file or interactively, are considered part of a module called `__main__`, so they have their own global namespace. 

### 9.2.1 Scopes and Namespaces Example
```py
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam

print("In global scope:", spam)
# In global scope: global spam
```

## 9.3 A First Look at Classes
### 9.3.1 Class Definition Syntax
skip

### 9.3.2 Class Objects
```py
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i
# (3.0, -4.5)
```

### 9.3.3 Instance Objects
Instance of a class.

### 9.3.4 Method Objects
skip

### 9.3.5 Class and Instance Variables
Instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class:
```py
class Dog:
    kind = 'canine'         # class variable shared by all instances
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
# 'canine'
>>> e.kind                  # shared by all dogs
# 'canine'
>>> d.name                  # unique to d
# 'Fido'
>>> e.name                  # unique to e
# 'Buddy'
```

## 9.4 Random Remarks
skip

## 9.5 Inheritance
derived class definition looks like this:
```py
class DerivedClassName(BaseClassName):
    # ...

# when the base class is defined in another module:
class DerivedClassName(module_name.BaseClassName):
    # ...
```

Method references are resolved as follows: the derived class is searched, then base classes if necessary.

Derived classes may override methods of their base classes.

An overriding method in a derived class may in fact want to extend, rather than simply replace the base class method. To call the base class method directly: `BaseClassName.method_name(self, arguments)`.

Python has two built-in functions that work with inheritance:
- `isinstance(obj_name, type_name)` - check an instance's type.
- `issubclass(class_name, base_class_name)` - check class inheritance.

### 9.5.1 Multiple Inheritance
A class definition with multiple base classes:
```py
class DerivedClassName(Base1, Base2, Base3):
    # ...
```

In the simplest cases, the search for attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy.

## 9.6 Private Variables
"Private" instance variables that cannot be accessed except from inside an object don't exist in Python. However, there is a convention that is followed by most Python code: a name (function/method/data member) prefixed with an underscore (e.g. `_spam`) should be treated as a non-public part of the API. It should be considered an implementation detail, and subject to change without notice.

Since there is a valid use-case for class-private members (namely to avoid name clashes of names with names defined by subclasses), there is limited support for such a mechanism, called "name mangling": Any identifier of the form `__spam` (at least 2 leading underscores, at most 1 trailing underscore) is textually replaced with `_classname__spam`, where `classname` is the current class name with leading underscore(s) stripped. This mangling is done regardless to the position of the identifier, as long as it occurs within the definition of a class.

Name mangling is helpful for letting subclasses override methods, without breaking intraclass method calls:
```py
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```

The above example would work even if `MappingSubclass` were to introduce a `__update` identifier, since it is replaced with `_Mapping__update` in the `Mapping` class, and `_MappingSubclass__update` in the `MappingSubclass` class, respectively.

Note that the mangling rules are designed mostly to avoid accidents; it still is possible to access or modify a variable that is considered private. 

## 9.7 Odds and Ends
To have a data type bundling together a few named data items, use `dataclasses`:
```py
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

john = Employee('john', 'computer lab', 1000)
john.dept # 'computer lab'
john.salary # 1000
```

## 9.8 Iterators
Most container objects can be looped over using a "for" statement. 

Behind the scenes, the for statement calls `iter()` on the container object. The function returns an iterator object that defines the method `__next__()` which accesses elements in the container one at a time. When there are no more elements, `__next__()` raises a `StopIteration exception`, which tells the for loop to terminate. You can call the `__next__()` method using the `next()` built-in function:
```py
s = 'abc'
it = iter(s)
it # <str_iterator object at 0x10c90e650>
next(it) # 'a'
next(it) # 'b'
next(it) # 'c'
next(it)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     next(it)
# StopIteration
```

To add iterator behavior to your classes:
```py
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
  
rev = Reverse('spam')
iter(rev) # <__main__.Reverse object at 0x00A1DB50>
for char in rev:
    print(char)
# m
# a
# p
# s
```

## 9.9 Generators
Generators are used for creating iterators. They are written like regular functions, but use the `yield` statement whenever they want to return data. Each time `next()` is called on it, the generator resumes where it left off - it remembers all the data values and which statement was last executed:
```py
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)
# f
# l
# o
# g

```

- Anything that can be done with generators can also be done with class-based iterators as described in the previous section. 
- What makes generators so compact is that the `__iter__()` and `__next__()` methods are created automatically. 
- the local variables and execution state are automatically saved between calls.
- When generators terminate, they automatically raise StopIteration.

## 9.10 Generator Expressions
```py
sum(i*i for i in range(10)) # 285

list1 = [10, 20, 30]
list2 = [7, 5, 3]
sum(x*y for x,y in zip(list1, list2)) # 260

unique_words = set(word for line in page  for word in line.split())

valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))
# ['f', 'l', 'o', 'g']

```
