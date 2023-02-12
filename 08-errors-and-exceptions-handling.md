# 8. Errors and Exceptions handling
Someone may use your code in an unexpected way. Error handling can plan for possible errors. With error handling, the code can continue with rest of the code, without having to stop the entire script. 

3 keywords for error handling:
- `try`: the block of code to be attempted
- `except`: the block of code that will be run if the try block has error
- `finally`: the block of code that will always be run, regardless of error

## Unit testing
As you begin to expand to larger multi-file projects, it becomes important to have tests in place. So as you make changes or update your code, you can run your test files to make sure previous code still runs as expected. 

There are different testing tools, such as:
- pylint: a library that looks at your code and reports back possible issues
- unittest: a built-in library that allow you to test your own programs and check you are getting desired outputs. 

In the terminal, `pip install pylint`. 

create a python file simple1.py: 
```python
a = 1
b = 2
print(a)
print(B)  # make a mistake on purpose
```
In the terminal, 
```console
isa@mac16 ~/D/python (main)> pylint examples/04-unit-testing/simple1.py 
************* Module simple1
examples/04-unit-testing/simple1.py:1:0: C0114: Missing module docstring (missing-module-docstring)
examples/04-unit-testing/simple1.py:1:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
examples/04-unit-testing/simple1.py:2:0: C0103: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)
examples/04-unit-testing/simple1.py:4:6: E0602: Undefined variable 'B' (undefined-variable)

-----------------------------------
Your code has been rated at 0.00/10
```

The last line shows an error with undefined variable 'B'. 

Now create a python file simple2.py, with better var names etc:
```python
'''
A very simple script. 
'''


def myfunc():
    '''
    A simple function
    '''
    first = 1
    second = 2
    print(first)
    print(second)


myfunc()
```

Run pylint again:
```console
lisa@mac16 ~/D/python (main) [18]> pylint examples/04-unit-testing/simple2.py
************* Module simple2
examples/04-unit-testing/simple2.py:2:21: C0303: Trailing whitespace (trailing-whitespace)

-----------------------------------
Your code has been rated at 8.33/10
```










