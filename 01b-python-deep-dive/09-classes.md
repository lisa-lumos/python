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
### 9.3.2 Class Objects
### 9.3.3 Instance Objects
### 9.3.4 Method Objects
### 9.3.5 Class and Instance Variables
## 9.4 Random Remarks
## 9.5 Inheritance
### 9.5.1 Multiple Inheritance
## 9.6 Private Variables
## 9.7 Odds and Ends
## 9.8 Iterators
## 9.9 Generators
## 9.10 Generator Expressions