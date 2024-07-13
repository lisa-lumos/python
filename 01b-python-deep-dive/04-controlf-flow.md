# 4. More Control Flow Tools
## 4.1 if Statements
```py
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
```
## 4.2 for Statements
Iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence. 
```py
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
```

Code that modifies a collection while iterating over that same collection can be tricky to get right. Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection:
```py
# Create a sample collection
users = {'Hans': 'active', 'Andy': 'inactive', 'John': 'active'}

# Strategy 1:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy 2:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
```

## 4.3 The range() Function
In many ways the object returned by range() behaves as if it is a list, but in fact it isn't. It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn't really make the list, thus saving space.

```py
list(range(0, 10, 3))
# [0, 3, 6, 9]
```

We say such an object is iterable, that is, suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted. We have seen that the for statement is such a construct, while an example of a function that takes an iterable is sum():
```py
sum(range(4))  # 0 + 1 + 2 + 3
# 6
```

## 4.4 break and continue Statements, and else Clauses on Loops
The break statement breaks out of the innermost enclosing `for` or `while` loop.

A `for` or `while` loop can include an `else` clause.
- In a `for` loop, the else clause is executed after the loop reaches its final iteration.
- In a `while` loop, it's executed after the loop's condition becomes false.
- In either kind of loop, the `else` clause is not executed if the loop was terminated by a `break`.

Look closely: the else clause belongs to the for loop, not the if statement:
```py
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2
# 5 is a prime number
# 6 equals 2 * 3
# 7 is a prime number
# 8 equals 2 * 4
# 9 equals 3 * 3
```

The `continue` statement, also borrowed from C, continues with the next iteration of the loop. 

## 4.5 pass Statements
The pass statement does nothing. It can be used when a statement is required syntactically, but the program requires no action. For example:

```py
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)

# This is commonly used for creating minimal classes:
class MyEmptyClass:
    pass

# As a place-holder for a function or conditional body 
# when you are working on new code, 
# allowing you to keep thinking at a more abstract level. 
# The pass is silently ignored:
def initlog(*args):
    pass   # Remember to implement this!
```

## 4.6 match Statements
```py
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403 | 404: # can combine
            return "Not allowed"
        case 418:
            return "I'm a teapot"
        case _: # "_" is a wildcard, and never fails to match
            return "Something's wrong with the internet"

# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y): # y gets assigned the val of 2nd val in the tuple
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

# If you are using classes to structure your data,
# you can use the class name followed by an argument list,
# (resembling a constructor), 
# but with the ability to capture attributes into variables
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
```
## 4.7 Defining Functions
The first statement of the function body can optionally be a string literal; this string literal is the function's "documentation string", or docstring. There are tools which use docstrings to automatically produce documentation, or to let the user interactively browse through code; `it's good practice to include docstrings in code that you write, so make a habit of it.`
```py
# write Fibonacci series up to n
def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
```

Arguments are passed using call by value (where the value is always an object reference, not the value of the object). 

When a function calls another function, or calls itself recursively, a new local symbol table is created for that call.

A method is a function that belongs to an object, and is named "obj.method_name".

## 4.8 More on Defining Functions
### 4.8.1 Default Argument Values
The most useful form is to specify a default value for one or more arguments. This creates a function that can be called with fewer arguments than it is defined.

The default values are evaluated at the point of function definition in the defining scope (top-down), and is evaluated only once. 

### 4.8.2 Keyword Arguments
Functions can also be called using keyword arguments:
```py
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
  
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
```

In a function call, keyword arguments must follow positional arguments. 

`**name` receives a dictionary, `*name` receives a tuple. `*name` must occur before `**name`.
```py
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.", # goes into the tuple
           shopkeeper="Michael Palin",    # goes into the dict
           client="John Cleese",          # goes into the dict
           sketch="Cheese Shop Sketch")   # goes into the dict
```

### 4.8.3 Special parameters
You can restrict the way a function arguments can be passed, either by:
- case1: positional-only
- case2: keyword-only
- case3: positional and keyword both allowed. 

If `/` and `*` are not present in the function definition, it  case3.  

Parameters before the `/` are positional only, and parameters after it are positional-or-keyword, or keyword-only.

Parameters following the `*` are keyword-only.

```py
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
```

### 4.8.4 Arbitrary Argument Lists

### 4.8.5 Unpacking Argument Lists

### 4.8.6 Lambda Expressions

### 4.8.7 Documentation Strings

### 4.8.8 Function Annotations

## 4.9 Intermezzo: Coding Style

