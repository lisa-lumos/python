# 8. Errors and Exceptions handling
Someone may use your code in an unexpected way. Error handling can plan for possible errors. With error handling, the code can continue with rest of the code, without having to stop the entire script. 

3 keywords for error handling:
- `try`: the block of code to be attempted
- `except`: the block of code that will be run if the try block has error
- `finally`: the block of code that will always be run, regardless of error

```py
def add(n1, n2):
    print (n1 + n2)
num1 = 1
num2 = '2'
try: 
    add(num1, num2)
except:
    print('Error adding two numbers!')
# Error adding two numbers!
try: 
    add(num1, num2)
except: # runs if try block has error
    print('Error adding two numbers!')
else: # runs if try block had no issue
    print("Add went well!")
finally:
    print("I run anyway!")
# Error adding two numbers!
# I run anyway!

try: 
    f = open('testfile.txt', 'w') # write mode
    f.write("Write a test line")
except TypeError:
    print("There was a type error! ")
except OSError:
    print("You have an OS Error! ")
finally:
    print('I always run!')
# I always run!

try: 
    f = open('testfile.txt', 'r') # read mode
    f.write("Write a test line")
except TypeError:
    print("There was a type error! ")
except OSError:
    print("You have an OS Error! ")
except: # catch anything else
    print("All other exceptions! ")
finally:
    print('I always run!')
# You have an OS Error! 
# I always run!

def ask_for_int():
    try: 
        result = int(input('Please provide a number: '))
    except:
        print("That is not a number. ")
    finally: 
        print("End of the block. ")
ask_for_int() # provide 20 as input
# End of the block.
ask_for_int() # provide a as input
# That is not a number. 
# End of the block.  

def ask_for_int():
    while True:
        try: 
            result = int(input('Please provide a number: '))
        except:
            print("That is not a number. ")
            continue
        else: 
            print('Yes, thank you')
            break
        finally:
            print('End of one loop')
ask_for_int() # provide 20
# Yes, thank you
# End of one loop
ask_for_int() # provide a, then 2
# That is not a number. 
# End of one loop
# Yes, thank you
# End of one loop
```

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

To do a unit test for a function in cap.py:
```python
def cap_text(text):
    '''
    Input a string
    Output the capitalized string
    '''
    # return text.capitalize()
    return text.title()

```

Create a testing file test_cap.py:
```
import unittest
import cap

class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
    unittest.main()

```

Run it in terminal, it shows that is passed both of the tests:
```console
(base) lisa@mac16 python % /opt/homebrew/bin/python3.11 /Users/lisa/Desktop/python/examples/04-unit-testing/test_cap.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```






