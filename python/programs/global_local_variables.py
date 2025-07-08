#variables that are created outside the defined function is called a global variable.
#It can be used in both inside and outside of a function.

#example

x = 'global variable' #It is a global variable.
print(x)

def myfunc():
    x = 'local variable' #It is a local variable.
    print(f'It is a {x}')
    
myfunc()
print('It is a ', x)

#variables that are created inside a function is known as local variables.
#it cannot be used oustside the function.
x = 'global variable' #It is a global variable.
print(x)

def myfunc():
    x = 'local variable' #It is a local variable.
    print(f'It is a {x}')
    
myfunc()
print('It is a ', x)


#for accessing the global variable inside the function instead of local variable by using a 'GLOBAL' keyword is used.

#Example
x = 'global variable' #It is a global variable.
print(x)

def myfunc():
    global x #updates the global variables
    x = ' modified local variable' #It is a local variable.
    print(f'It is a {x}')
    
myfunc()
print('It is a', x)
 


 