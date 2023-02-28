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





```


























