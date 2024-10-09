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

# to force a specified exception to occur:
raise NameError('HiThere')


```

## 8.4 Raising Exceptions
## 8.5 Exception Chaining
## 8.6 User-defined Exceptions
## 8.7 Defining Clean-up Actions
## 8.8 Predefined Clean-up Actions
## 8.9 Raising and Handling Multiple Unrelated Exceptions
## 8.10 Enriching Exceptions with Notes








