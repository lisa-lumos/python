# 9. Python Decorators and Generators
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
























