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

```py
def say_hello():
    print("Hello")
    print("Round! ")
say_hello()

def say_hello(name):
    print(f"Hello {name}")
say_hello("Lisa")

def say_hello(name='Default name'): # provide a default val for argument
    print(f"Hello {name}")
say_hello()

def add_num(num1, num2): # a function that returns something
    return num1 + num2
my_sum = add_num(1, 2)
print(my_sum)
add_num('a', 'b') # ab # when inputs are not numbers # Python is dynamically typed, so if create a function that other people use, better check the datatype first

def even_check(number): # check whether a number is even
    return number % 2 == 0
print(even_check(4)) # True
print(even_check(5)) # False

def even_check_list(num_list): # check whether list has a num that is even
    for num in num_list:
        if num % 2 == 0:
            return True
    return False
print(even_check_list([1, 3, 5])) # False

def return_even_vals(num_list): # return vals in a list that is even
    result = []
    for num in num_list:
        if num % 2 == 0:
            result.append(num)
    return result
print(return_even_vals([1, 2, 3, 5, 7, 8])) # [2, 8]

stock_prices = [('APPL', 200), ('GOOG', 300), ('MSFT', 100)]
for ticker, price in stock_prices: # use tuple unpacking
    print(ticker)
# APPL
# GOOG
# MSFT
def price_check(stock_prices_list): # return the tuple with max price
    cur_max = 0
    max_ticker = ''
    for ticker, price in stock_prices_list:
        if price > cur_max:
            cur_max = price
            max_ticker = ticker
    return (max_ticker, cur_max)
print(price_check(stock_prices)) # ('GOOG', 300)
ticker_name, price = price_check(stock_prices) # get result using tuple unpacking, could get error if num of items in tuple not match the num of vars on the left hand side

my_list = [1, 2, 3, 4, 5, 6, 7]
from random import shuffle
shuffle(my_list) # shuffle the list in-place, so returns nothing
def shuffle_list(input_list): # a function that returns shuffled result
    shuffle(input_list)
    return input_list
print(shuffle_list(my_list)) # [4, 5, 2, 1, 6, 7, 3]

# in below function, a and b are positional arguments
def myfunc(a, b): # return 5% of (a+b)
    return sum((a, b)) * 0.05
print(myfunc(40, 60)) # 5.0

# *args allows to take multiple arguments, and internally convert into a tuple
def myfunc(*args):
    return sum(args) * 0.05
print(myfunc(40, 60, 100)) # 10.0

# it is the * that matters, you can use other names, 
# but it is best practice to use *args for readability
def myfunc(*vals):
    return sum(vals) * 0.05

# **kwargs allows to take a key-val pairs, and internally convert to a dictionary
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"My fruit is {kwargs['fruit']}")
    else: 
        print('no fruit')
print(myfunc(fruit='apple')) # My fruit is apple
print(myfunc(fruit='apple', veggie='cabbage')) # # My fruit is apple

def myfunc(*args, **kwargs): # you can use both of them in one function
    print(f"I would like {args[0]} {kwargs['food']}. ")
print(myfunc(1, 2, 3, food='sandwich', fruit='orange')) # I would like 1 sandwich. # note that args should come ahead of kwargs, because location of both of them is defined

def square(num):
    return num**2
my_nums = [1, 2, 3, 4, 5]
for item in map(square, my_nums): # apply the func to each elem in the array
    print(item)
# 1
# 4
# 9
# 16
# 25
print(list(map(square, my_nums))) # [1, 4, 9, 16, 25] # return the result as a list

def check_even(num):
    return num%2 == 0
my_nums = [1, 2, 3, 4, 5, 6]
print(list(filter(check_even, my_nums))) # [2, 4, 6] # filter takes a func that returns true or false

# lambda expression (anonymous function)
print(lambda num: num**2) # <function __main__.<lambda>(num)>
list(map(lambda num:num**2, my_nums)) # [1, 4, 9, 16, 25, 36]
list(filter(lambda num: num%2 == 0, my_nums)) # [2, 4, 6]

name = 'a global string' # global var
def greet():
    name = "Sammy"  # enclosing function local
    def hello(): 
        name = 'Lisa' # local var
        print(f"hello {name}")
    hello()
greet() # hello Lisa

name = 'a global string' # global var
def greet():
    name = "Sammy"  # enclosing function local
    def hello(): 
        print(f"hello {name}")
    hello()
greet() # hello Sammy

name = 'a global string' # global var
def greet():
    def hello():
        print(f"hello {name}")
    hello()
greet() # hello a global string

x = 50
def func():
    global x # declare x as global, so you can reach out to global namespace
    print(f'val of x is {x}')
    x = 200
    print(f'val of x is updated globally to {x}')
func()
# val of x is 50
# val of x is updated globally to 200
print(f'val of x is finally {x}')
# val of x is finally 200

# To avoid accidentally overriding global keyword in a large script, 
# recommend to avoid using global keyword, 
# and write the function to be like x = func(x) to update x. 
```

LEGB Rule (order that python look for variables in):
- L: Local - var declared in a function that are not declared global in that function
- E: Enclosing function locals - for function inside a function, inner to outer
- G: Global (module) - vars assigned at the top level of a module file, or declared as global in a function in this file
- B: Built-in (Python) - open, range, SyntaxError, ...