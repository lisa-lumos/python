# 8. Errors and Exceptions
## 8.1 Syntax Errors
skipped

## 8.2 Exceptions
Errors detected during execution are called exceptions. 

## 8.3 Handling Exceptions
Handle selected exceptions:
```py
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except (RuntimeError, TypeError, NameError): # can have more except clauses
        pass

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # <class 'Exception'>
    print(inst.args)     # ('spam', 'eggs')
    print(inst)          # ('spam', 'eggs')
    x, y = inst.args     # unpack args
    print('x =', x)      # x = spam
    print('y =', y)      # y = eggs


```

The most common pattern for handling Exception, is to print/log the exception, and then re-raise it (allowing a caller to handle the exception as well):
```py
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

The use of the else clause is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn't raised by the code being protected by the try ... except statement:
```py
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

```

## 8.4 Raising Exceptions
```py
# to force a specified exception to occur:
raise NameError('HiThere')

raise
```

## 8.5 Exception Chaining
If an unhandled exception occurs inside an except section, it will have the exception being handled attached to it, and included in the error message. 

You can disable automatic exception chaining using the `from None` idiom. 

## 8.6 User-defined Exceptions
You can name your own exceptions by creating a new exception class. 

## 8.7 Defining Clean-up Actions
If a `finally` clause is present, it will execute as the last task before the try statement completes. It runs whether or not the try statement produces an exception.
```py
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

# if the try statement reaches a break, continue or return statement, 
# the finally clause will execute just prior to the statement above.
def bool_return():
    try:
        return True
    finally:
        return False

bool_return() # False


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)
# result is 2.0
# executing finally clause
divide(2, 0)
# division by zero!
# executing finally clause
divide("2", "1")
# executing finally clause
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 3, in divide
# TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

In real world applications, the `finally` clause is useful for releasing external resources (such as files or network connections), regardless of whether the use of the resource was successful.

## 8.8 Predefined Clean-up Actions
The `with` statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly, even if a problem was encountered while processing the lines.
```py
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```
## 8.9 Raising and Handling Multiple Unrelated Exceptions

## 8.10 Enriching Exceptions with Notes








