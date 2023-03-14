# 9. Python Decorators and Generators

## Decorators
Decorators allow you to decorate a function (turn on/off extra functionality to an already existing function). They use the @ operator are then placed on top of the original function. 

```py
def func():
    return 1

func()

def hello():
    return "Hello!"

hello()

greet = hello # point greet to the function object
greet() # return same with hello()

del hello
hello() # return 'hello' not defined
greet() # returns "Hello!". Because functions are objects that can be passed into other objects. 

def hello(name='lisa'):
    print('the hello() function is executed. ')

hello()

def hello(name='lisa'):
    print('the hello() function is executed. ')
    def greet():
        return '\t this is the greet() func inside hello(). '

    def welcome():
        return '\t this is the welcome() func inside hello(). '
    
    print(greet()) # cannot access it outside of hello function, because of scope
    print(welcome())
    print('This is the end of the hello() function. ')

hello()

def hello(name='lisa'):
    print('the hello() function is executed. ')
    def greet():
        return '\t this is the greet() func inside hello(). '

    def welcome():
        return '\t this is the welcome() func inside hello(). '

    print('I am going to return a function. ')
    if name == 'lisa':
        return greet
    else:
        return welcome

my_new_func = hello('lisa')
my_new_func()

def hello():
    return "Hi lisa"

# pass a function into a new function
def other(some_func):
    print(some_func())

other(hello) # prints "Hi lisa"

def new_decorator(original_func):
    def wrap_func():
        print('Some new code before the original function')
        original_func()
        print('Some new code after the original function')
    return wrap_func

def func_needs_decorator():
    print("I want to be decorated! ")

decorated_func = new_decorator(func_needs_decorator)
decorated_func() # runs the new function

@new_decorator # this passes the below function into the previously defined new_decorator() function. If want to remove the decorations later on, just comment this line. 
def func_needs_decorator(): # This is the one that will be wrapped around
    print("I want to be decorated! ")
func_needs_decorator() # runs the new function
```

Realistically, you will not write the new_decorator function. Instead, you will be using a web framework or someone else's library, and only need to prepend the `@new_decorator` row to render a new website or point to another page. It is commonly used in web frameworks such as Django or Flask. 

## Generators - the yield keyword
Generator functions allow us to write a function that can send back a value and then automatically resume to pick up where it left off. In this way, we can generate a sequence of values over time. => more memory efficient. 

The advantage: instead of having to compute an entire series of values up front, the generator computes one value, and waits until the next values is called for. 

This is what range() function does. It keeps track of the last number and the step size, to provide a flow of numbers. It doesn't produce a giant list at once in memory. If a user does need the list, they need to transform the generator to a list, like `list(range(0, 10))`. 

```python
def create_cubes_v1(n): # generates the list in memory as a whole
    result = []
    for x in range(n):
        result.append(x**3)
    return result

print(create_cubes_v1(10)) # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

def create_cubes_v2(n): # the memory efficient way
    for x in range(n):
        yield x**3

for x in create_cubes_v2(10):
    print(x)

print(list(create_cubes_v2(10)))  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

def gen_fib(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

print(list(gen_fib(10))) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def simple_gen():
    for x in range(3):
        yield x

for x in simple_gen(): # 0 1 2
    print(x)

g = simple_gen()
print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 2
print(next(g)) # StopIteration Error. Note we don't get this error in "for loop" because it automatically catches the error. 

s = 'hello'
for letter in s: # h e l l o
    print(letter)

next(s) # TypeError: 'str' is not an iterator
s_iter =  iter(s)
print(next(s_iter)) # h
print(next(s_iter)) # e
```













