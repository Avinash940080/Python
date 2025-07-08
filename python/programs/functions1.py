# Python Functions

# A function is a block of code which only runs when it is called
# You can pass data, known as parameters, into a function.
# A functiom can return data as a result.

# Creating a Function:
# In python a function is defined using the 'def' keyword.

# Example:
def my_func():
    print('hello world')

my_func()   # Calling a function and printing it.

# Arguments:
# Information can be passed into functions as arguments.
# func(arguments):
# It is also known as parameters.

# Example:
def my_func(fname):
    print('hello '+fname)

my_func('tony')


# Number of arguments.
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, 
# you have to call the function with 2 arguments, not more, and not less.

# Example:
def func(fname,lastname):
    print('hello '+fname+' '+lastname)
func('Avinash', 'Pachimadla')


# Arbitary Arguments, *args:
# If you don't know how many arguments that will be passed into our function,
# add a '*' before the parameter named in the function definition.
# def func(*parameter)

# Example:

def func1(*kids):
    print('the youngest child is ' + kids[1]) 

func1('emil','tobias','linus')


# Keyword arguments:
# We can also send arguments with the key=value syntax.
# This way the order of the arguments does not matter.
# It is often shortened as kwargs

# Example;
def greet(fname,lname, greet='hello'):
    print(f'{greet} {fname} {lname}')

greet('john', 'wick',greet='hello')

greet('john', 'wick',greet='hi') # here we can change the greet value.



# Arbitary keyword arguments:
# If we don't know how many keyword arguments that will be passed into your function, add two asterik '**' before the name in the function.

# Example:
def func2(**kids):
    print('his first name is ' + kids['fname']) 
    print('his first name is ' + kids['lname'])

func2(fname = 'John', lname = 'wick')


# Default parameter value;
# If we call a function without argument, it uses the default value.

# Example:
def country(country='Norway'):
    print('I am from ', country)
country('India')
country() # It uses the default value i.e. is Norway


# Passing a List as an Argument:
# We can send any data types of argument to a function and it will be treated as the same data type inside the function.

# Example-1:
def item(food):
    for x in food:
        print(x)

fruits = ['apple', 'banana', 'guava']
item(fruits)

# Example-2:
def print_list(elements):
    for i in range(len(elements)):
        values = map(int, input('enter the values separated by comma: ').split(','))
        elements[i] = list(values)
        print(elements[i])
        print(elements)

my_list=[None]*1
print_list(my_list)


# Return values:
# To let a function return a value, use the 'return' statement:

# Example:
def calc(num):
    return 5 * num

print(calc(5))
print(calc(4))
print(calc(3))
print(calc(2))

# Pass statement:
# function definitions cannot be empty, but if you for some reasons have a function definitions with no content, 
# put in the 'pass' statement to avoid getting an error.


def my_function():
    pass


# Positional - Arguments:

# When we define a function, you can specify parameters. When you call this function,  you provide arguments. 
# Positional arguments are assigned to parameters based on their position in the function call.
# The first argument is assigned to the first parameter, the second agrument to the second paramneter, and so on.

# Example:
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info("Alice", 30)  # Outputs: Name: Alice, Age: 30
display_info(30, "Alice")  # Outputs: Name: 30, Age: Alice (incorrect order)

# All positional arguments must be provided when calling the function, unless the parameters have default values.

# Example:
def introduce(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

introduce("Bob")          # Outputs: Hello, Bob!
introduce("Bob", "Hi")    # Outputs: Hi, Bob!


# Positional - Only Arguments.
# You can specify that a function can have only positional arguments, or only keyword arguments.
# To specify that a function can have only positional arguments, add ', /' after the arguments.

# Example:
def pos_only(a, /):
    print(a)

pos_only(3)

# It returns error if we try to pass keyword first.
# Example
def pos_only(a, /):
    print(a)

 # pos_only(a = 2)  It returns error.


 # Keyword-Only Arguments:
 # To specify that a function ca have only keyword arguments, add '*, 'before the arguments.

 # Example:
def key_only(*, a):
    print(a)

key_only(a=10)


# It returns error if we try to pass any other arguments other than keyword arguments.
# Example:
def key_only(*, a):
    print(a)

# key_only(10) It returns an error.


# Combine Positional - Only and keyword - Only:
# We can combine the two arguments types in the same function.
# Any argument before the '/ ,' are positional-only arguments, and any argument after the '*, ' are keyword-only arguments.

# Example:
def comb(a, b, /, * ,c ,d):
    print(a+b-c+d)

comb(5, 6, c=5, d=6)


# It returns error if we try to pass the arguments in a different order.
# Example:
def comb(a, b, /, *,c ,d):
    print(a+b-c+d)

# comb(a=5, b=6, 5, 6) It returns error as the keywords are passed before the position arguments.



