#varibles are containers for storing data values.
#example
x=5
print(x)
#adding two variables
x=4
y=6
print(x+y)
if 5>10:
   print('true')
else:
    print('false')
#printing type of variables
x='hello'
print(type(x))
#varaible names
'''
short name
case sensitive(HI,Hi,hi,hI are different variables)
no python keywords
can start with a underscore
'''
Car='mercedesAMG'
print(Car)

#assigning multiple values to multiple variables
x, y, z = ['apple','banana','orange'] 
print(x)
print(y)
print(z)

x=y=z = 'orange'
print(x)
print(y)
print(z)


fruits = ['apple','banana','orange']
x ,y ,z = fruits
print(x)
print(y)
print(z)
x = int(3)
print(x)
print(type(x))