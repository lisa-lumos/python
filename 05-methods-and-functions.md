# 5. Methods and Functions

## Methods
Methods are functions that are built into objects. 

Documentation: `https://docs.python.org/3/`. 

## Functions
### def Keyword
To create a function in Python. Conventionally function names use snake casing, such as `name_of_function`. 
```python
def name_of_function():
    '''
    This is a multi line comment (Docstring)
    '''
    print("Hello")
```
Call this function by: `name_of_function()`

```python
def name_of_function(name):
    '''
    This is a multi line comment (Docstring)
    '''
    print("Hello " + name)
```
Call this function by: `name_of_function("Lisa")`

You can also use return in a function, which allow you to save the result to a variable. 
```python
def add_function(num1, num2):
    '''
    This is a multi line comment (Docstring)
    '''
    return num1 + num2
```
Call this function by: `num3 = add_function(1, 2)`. 

















