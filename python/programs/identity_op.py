#Identity operators are used to compare the memory locations of the two objects to check if they refer to the same object. 
#There are two operators in python.

'''
is operator - Returns true if both the variables are the same objects.
is not operator - Returns true if both the variables are not the same objects.

'''

#example

a = 10
b = 10

a == b #It refers that the both variables share the same memory location.

print(a is b)# it returns true for the integers ranging from (-5 to 256) or else it doesnot share same memory location.


a = [1, 2, 3]
b = [1, 2, 3]

a == b #It returns false although it has same values because they doesnot share same object memory location.

print(a is b) #it returns false


#Example

a = 10
b = 10

a == b 

print(a is not b) #It returns false as they are sharing same memory location.


a = [1, 2, 3]
b = [1, 2, 3]

a == b

print(a is not b) #it returns true as they are not sharing the same memory location.