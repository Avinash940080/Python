# -------------------------------------------------> Object Oriented Programming: <---------------------------------------------------------------------

# OOPs concept is used to map real world entities.
# There are objects and classes in python.

# ----------------> Class: <-------------------
# Think of a class as a blueprint or a template. 
# It defines the structure and behaviour(data and methods) that objects created from the class will have.
# It is like an objects constructor, or a 'blueprint' for creating objects.

# Example:
# To create a class, we use the keyword 'class':
class myclass:
    name = 'avinash'
    age = 20


# -----------------> Objects: <-----------------
# Object is a combination of properties and methods.
# Almost everything in Python is an object, with its properties and methods.
# Objects is an instance of the class used to access the properties of the class.
# Now lets create an object of the class.

# Example:
class myclass:
    name = 'avinash'
    age = 20

object = myclass()
print(object.name)
print(object.age)

# ---------------> CONSTRUCTORS <----------------

# __init__method:

# The purpose of __init__ method is used to initialize the object's state. It's called when an object is created.

# ------> SPECIAL-METHOD <--------
# The __init__ method is a special method in Python. It's known as a constructor.
# It is named using double underscores before and after(__), which signifies its specifies status in Python.


# -------> PARAMETERS <------------
# The '__init__' method can accept any number of parametes, but the first parameter must always be 'self'.
# 'self' refers to the instance of the class, allowing you to access the class attributes.


# -------> INITIALIZATION <--------
# Within the __init__ method, you can set initial values for the object's attributes by using 'self.attribute_name'.


# -------> 'self' parameter <--------
# The 'self' parameter is an essential part of classes in Python.
# It allows us to access the attributes and methods of the class in Python.
# It acts as a reference to the instance of the class.

# Syntax
'''

class MyClass:
def __init__(self, attribute1, attribute2):
    self.attribute1 = attribute1
    self.attribute2 = attribute2

'''


# Example:

class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    def introduce(self):
        return f'It is a {self.name} {self.model}'
    
car1 = Car('BMW', 'M5')

print(car1.introduce())
        

# ----> The __str()__ Function:

# The '__str__()' function controls what should be returned when the class object is represented as a string.
# If the '__str()__' function is not set, the string representation of the object is returned.
# It is a special method that provides a readable and understandable string representation of an object. When we print the object the method is called.


# Example:

class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    def __str__(self):
        return f'This is a {self.name} {self.model}'
    
car1 = Car('keonigsegg', 'jesko absolut')
print(car1)


# -----> Object-Methods:
# Objects can also contain methods. Methods in objects are functions that belong to the object.
# We can create multiple functions in a class that can be called.

# Example:
class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    def details(self):    # Here we defined a function called details
        return f'It is a {self.name} {self.model}'

car1 = Car('BMW', 'M5 COMPETITION')
print(car1.details())


# -----> Modify Object Properties:
# We can modify properties of an objects by referring to the object name and changing its property with a new value.
# syntax ->  obj_name.property = new value


# Example:
class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    def __str__(self):
        return f'This is a {self.name} {self.model}'
    
car1 = Car('BMW', 'M5 COMPETITION')
print(car1)
car1.model = 'M5 CS' # Here we changed the model of the car.
print(car1)


# -----> Delete object properties:
# We can delete the object properties using the del keyword.

# Example:
class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
    
    def __str__(self):
        return f'This is a {self.name} {self.model} manufactured in {self.year}'
    
car1 = Car('BMW', 'M5 COMPETITION', 2018)
print(car1)

del car1 # here, it deletes the object completely.


# -----> The pass Statement:
# 'class' definitions cannot be empty, but if we for some reason have a 'class' definition with no content, 
# put in the 'pass' statement to avoid getting an error.

# Example:
class Car:
    pass

