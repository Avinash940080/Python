#int
#float
#complex

#type conversion of numbers

x = 1
y = 2.45
z = 5j

print(type(x))
print(type(y))
print(type(z))

x = float(x)
print(x)
y = int(y)
print(y)
z = complex(z)  #we can't convert complex numbers to any type of numbers.
print(z)
y = complex(y)
print(y)

print(type(x))
print(type(y))
print(type(z))


#Scientific notation for respresting a number as a floating piont literal.
#examples

#e or E is used for representing the multiples of 10.
#for example 3.14e0 is same as 3.14*10**0
#similarily e1, e2 is used for 10**1, 10**2

#example program

floating_point = 3.14e0
print(floating_point)