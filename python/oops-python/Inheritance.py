# -------------------------------------------------------> Python Inheritance: <--------------------------------------------------------------------------

#  Inheritance allows us to define a class that inherits al the methods and properties from another class.
# 'Parent class' is the class being inherited from, also called base class.
# 'Child class' is the class that inherits fro another class, also called derived class.
#  syntax ----> 
'''
class Parentclass:
    pass
class Childclass(Parent class):
    pass

'''

# Example:
class employee:     # superclass
    def __init__(self, employee, id):
        self.employee = employee
        self.id = id
    def showdetails(self):
        print(f'{self.employee} has a id {self.id}')
class programmer(employee):     # subclass
    def language(self):
        print('the default language is python')

emp1 = employee('avinash', 545)
emp1.showdetails()
emp2 = programmer('GodsEye', 911)
emp2.showdetails()
emp2.language()


# --------------------> Types of Inheritance <--------------------
# There are 5 types of inheritance. They are:

# 1. Single Inheritance:
# -> In this, a subclass inherits from one super class.

# Example-1:
# Basic example:
class Parent:
    pass
class Child(Parent):
    pass


# Example-2:
# Example on real world entities:
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
class Dog(Animal):
    def showdetails(self, breed):
        self.breed = breed
        print(f'Animal Name: {self.name}, Species: {self.species}, Breed: {self.breed}')

a1 = Dog('Buddy', 'Canine')
a1.showdetails('Golden Retriever')

# 2. Multiple Inheritance:
# -> A subclass inherits from more than one superclass.

# Example-1:
# Basic example:
class parent1:
    pass
class parent2:
    pass
class child(parent1, parent2):
    pass

# Example-2:
# Example on real world entities:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Employee:
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary
class Manager(Person, Employee):
        def __init__(self, name, age, id, salary, department):
            Person.__init__(self, name, age)
            Employee.__init__(self, id, salary)
            self.department = department
        def show_manager_details(self):
            print(f'Name: {self.name}, Age: {self.age}, Employee id: {self.id}, Salary: {self.salary}, Department: {self.department}')

m1 = Manager('Alice', 35, 101, 75000, 'IT')
m1.show_manager_details()


# 3. Multilevel Inheritance:
# -> A subclass inherits from a superclass, and that superclass inherits from another superclass.

# Example-1:
class grandparent:
    pass
class parent(grandparent):
    pass
class child(parent):
    pass


# Example-2:
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def show_vehicle_details(self):
        print(f'It is a {self.make} {self.model}')

class Car(Vehicle):
    def __init__(self, make, model, doors):
        Vehicle.__init__(self, make, model)
        self.doors = doors
    def show_car_details(self):
        print(f'It has {self.doors} doors')

class ElectricCar(Car):
    def __init__(self, make, model, doors, battery):
     Car.__init__(self, make, model, doors)
     self.battery = battery

    def show_electric_car_details(self):
        print(f'It has a battery capacity of {self.battery}')
        print(f'Make: {self.make}, Model: {self.model}, Number of Doors: {self.doors}, Battery Capacity: {self.battery}')


car1 = ElectricCar('Tesla', 'Model S', 4, '100 kWh')
car1.show_vehicle_details()
car1.show_car_details()
car1.show_electric_car_details()



# 4. Hierarichal Inheritance:
# -> Multiple subclasses inherit from the same superclass.

# Example - 1:
class Parent:
    pass
class child1(Parent):
    pass
class child2(Parent):
    pass

# Example - 2:
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def showdetails(self):
        print(f'It is a {self.model}')

class Car(Vehicle):
    def features(self, doors):
        self.doors = doors
        print(f'It is a {self.make} {self.model} with {self.doors} doors')

class Bike(Vehicle):
    def features(self, type):
        self.type = type
        print(f'It is {self.make} {self.model} and is a {self.type} bike')

class Truck(Vehicle):
    def capacity(self, cap):
        self.cap = cap
        print(f'It is a {self.make} {self.model} with a {self.cap} capacity')


car1 = Car('toyota', 'supra', 1997)
car2 = Car('bmw', 'm5', 2018)
car1.features(5)
car2.features(5)
bike1 = Bike('kawasaki', 'z900', 2015)
bike1.features('race')
truck1 = Truck('Tata', 'Prima', 2018)
truck1.capacity('1 ton')


# 5. Hybrid Inheritance:
# -> A hybrid inheritance is a combination of two or more types of inheritance.

# Example:
class grandparent:
    pass
class parent(grandparent):
    pass
class child1(parent):
    pass
class child2(parent):
    pass
class child3(grandparent):
    pass



# super() function:
# Python has a super() function that will make the child class inherit 
# all the methods and properties from its parent.

# Example:
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

x = person('john', 'doe')
x.printname()

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)



