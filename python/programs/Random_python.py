#Random number
#random() is not a built in function in python so we use import random module for printing the random numbers
#example

import random

print(random.randrange(5, 10)) #It used to generate an integer between two integers including starting number and excluding ending number.


print(random.randint(5, 10)) #In this case both the integers are included unlike the above case.


print(random.random()) #It is used generate a random float number between o and 1.


print(random.uniform(0.20, 0.25)) #It is used to generate random float number between two given parameters.

my_list = [1, 'start', 'stop', 5, 6]
print(random.choice(my_list)) #It is used to print the random choices from the given list.

list = [1, 2, 3, 4, 5]
random.shuffle(list) #It is used to shuffle the given list
print(list)



r1 = random.uniform(4.5,5.2)
r1 = round(r1, 2) #round() is used for limiting the no of decimal places.
print(r1) # It is only one of the techniques for rounding up the decimal values.
