# OOP
Python allow users to create their own objects with their own attributes and methods. 

```python
class NameOfClass():
  def __init__(self, param1, param2):
    self.param1 = param1
    self.param2 = param2
  
  def some_method(self):
    print(self.param1)
```

Inheritance: form new classes using classes that have already been defined. 

Polymorphism: different classes can share the same method name, and the methods can be called from the same place, even though different objects can be passed in. 

Special methods allow us to use built in operations in Python, such as length function, or print function, with user created objects. 

```py
class Sample():
    pass
my_sample = Sample() # create an instance of this class
print(type(my_sample)) # <class '__main__.Sample'> # return the type of the instance

class Dog():
    def __init__(self, breed):
        self.breed = breed # initialize an attribute for this class
# my_dog = Dog() # wil return error if do not pass the param breed
my_dog = Dog(breed='Lab') # create an instance of this class
print(type(my_dog)) # <class '__main__.Dog'> # return the type of this class
print(my_dog.breed) # Lab # return the breed attribute of the instance

class Dog():
    def __init__(self, breed, name, spots): # more attributes
        self.breed = breed # initialize an attribute for this class
        self.name = name
        self.spots = spots
my_dog = Dog(breed='lab', name='sammy', spots=False)
print(my_dog.spots) # False

class Dog():
    animal_type = 'mammal' # class object attribute, same for all instances of this class
    def __init__(self, breed, name, spots): # more attributes
        self.breed = breed # initialize an attribute for this class
        self.name = name
        self.spots = spots
my_dog = Dog(breed='lab', name='sammy', spots=False)
print(my_dog.animal_type) # mammal

class Dog():
    animal_type = 'mammal' # class object attribute, same for all instances of this class
    def __init__(self, breed, name, spots): # more attributes
        self.breed = breed # initialize an attribute for this class
        self.name = name
        self.spots = spots
    def bark(self): # a method of this class
        print("Woof!")
my_dog = Dog(breed='lab', name='sammy', spots=False)
my_dog.bark() # Woof!

class Dog():
    animal_type = 'mammal' # class object attribute, same for all instances of this class
    def __init__(self, breed, name, spots): # more attributes
        self.breed = breed # initialize an attribute for this class
        self.name = name
        self.spots = spots
    def bark(self): # a method of this class, uses the class attribute
        print(f"Woof! My name is {self.name}")
my_dog = Dog(breed='lab', name='sammy', spots=False)
my_dog.bark() # Woof! My name is sammy

class Dog():
    animal_type = 'mammal' # class object attribute, same for all instances of this class
    def __init__(self, breed, name, spots): # more attributes
        self.breed = breed # initialize an attribute for this class
        self.name = name
        self.spots = spots
    def bark(self, my_number): # a method of this class, takes a variable
        print(f"Woof! My name is {self.name}, and my number is {my_number}")
my_dog = Dog(breed='lab', name='sammy', spots=False)
my_dog.bark(3) # Woof! My name is sammy, and my number is 3

class Circle():
    PI = 3.14
    def __init__(self, radius=1): # radius has a default value
        self.radius = radius
    def get_circumference(self):
        return self.radius * self.PI * 2
my_circle = Circle() # use default radius value
my_circle.get_circumference() # 6.28
my_circle = Circle(2) # use customized value
my_circle.get_circumference() # 12.56

class Circle():
    PI = 3.14
    def __init__(self, radius=1): # radius has a default value
        self.radius = radius
        self.area = self.PI * radius * radius
    def get_circumference(self):
        return self.radius * self.PI * 2
my_circle = Circle(2) # use customized value
my_circle.area # 12.56

class Circle():
    PI = 3.14  # can use Circle instead of self to refer class attribute
    def __init__(self, radius=1): # radius has a default value
        self.radius = radius
        self.area = Circle.PI * radius * radius
    def get_circumference(self):
        return self.radius * Circle.PI * 2

class Animal():
    def __init__(self):
        print("Animal created. ")
    def who_am_i(self):
        print("I am an animal. ")
    def eat(self):
        print("I am eating. ")
my_animal = Animal() # Animal created. 
my_animal.eat() # I am eating. 
class Dog(Animal): # derive the Animal class
    def __init__(self):
        Animal.__init__(self)
        print("Dog created. ")
    def who_am_i(self):
        print("I am a dog!")
    def bark(self):
        print("Woof! ")
mydog = Dog()
# Animal created. 
# Dog created. 
mydog.eat() # this dog instance can reuse the animal methods via inheritance
# I am eating. 
mydog.who_am_i() # it can overwrite the animal methods
# I am a dog!
mydog.bark() # it can add new methods
# Woof! 

class Dog():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + " says woof! "
class Cat():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + " says meow! "
niko = Dog("Niko")
felix = Cat("felix")
for pet in [niko, felix]: # example of polymorphism
    print(pet.speak())
# Niko says woof! 
# felix says meow! 
def pet_speak(pet):
    print(pet.speak())
pet_speak(niko)
pet_speak(felix)
# Niko says woof! 
# felix says meow!

class Animal(): # abstract class
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("this is an abstract method")
my_animal =  Animal('fred')
# my_animal.speak() # NotImplementedError 
class Dog(Animal):
    def speak(self):
        return self.name + ' says woof! '
fido = Dog('Fido')
fido.speak() # 'Fido says woof! '

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self): # return the string representation of the object
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages
mybook = Book('mytitle', 'myauthor', 100)
print(mybook) # mytitle by myauthor # this calls the __str__(self) 
print(str(mybook)) # mytitle by myauthor # this also calls __str__(self)
print(len(mybook)) # 100 # this calls __len__(self)
del mybook # delete the instance of this Book object, works without __del__() defined

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self): # return the string representation of the object
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages
    def __del__(self):
        print("A book object has been deleted. ")
mybook = Book('mytitle', 'myauthor', 100)
del mybook # A book object has been deleted. # now also calls __del__() , and delete the instance
```


















