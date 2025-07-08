# For loops.
# It is used for iterating over a sequence(like a list,tuple,dictionary,set,or string)
# This allows you to execute a block of code for each item in the sequence.

# Example
for i in range(1,4):
    print(f'{i}')


# Looping through a string.
# strings are iterable objects, they contain a sequence of characters

# Example
for x in 'apple':
    print(x)
    
# using break statement

# Example 1
for x in 'apple':
    print(x)
    if x == 'p' :
        print('hello')
        break

# Example 2 using break statement in a sequence.

list = ['apple','banana','potato','mango']

for x in list:
    print(x)
    if x == 'potato':
        break
    
# 'Continue' statement
# With the continue statement we can stop the current iteration of the loop and continue with the next

fruits = ['apple','banana','potato','mango']
for x in fruits:
    if x == 'potato':
        print(f'{x} is not a fruit')
        continue
    print(x)

# Range() function.
# To loop through a set of code a specified number of times, we can use the range() function.
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1(by default), and ends at a specified number.

# Example
n = 0
for i in range(1, 10):
    if i%2 == 0:
        n += 1
        print(i)
print(f'we have {n} even numbers')
    


# Using else in a loop.
# the else block will not be executed if the break statement is used before the else statement.

# Example
num = [1,2,3,4,-6,-7]
for x in num:
    if x>0:
        print(x)
    else:
        print(f'the negative number is: {x}')


# Nested loops.
# A nested loop is a loop inside a loop.
# The 'inner loop' is executed one time for each iteration of the 'outer loop'.

# Example
for x in range(3): #outer loop
    for y in range(3): #inner loop
        print(x, y)

# Example on sequence
color = ['black','red','blue']
items = ['sneakers','shirts','pants','sunglass']
for x in color:
    for y in items:
        print(x, y)

# The Pass statement
# for loops cannot be empty, if you for some reason have a for loop with no conten, put in the 'pass' statement to avoid getting an error.

# Example
for x in [1,2,3]:
    pass  #It helps in avoiding the error


# The enumerate() funtion.
# The enumerate() function in python helps you keep track of both the index and the value of intems in a list when you loop through it.

# Example
fruits = ['apple','banana','mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

