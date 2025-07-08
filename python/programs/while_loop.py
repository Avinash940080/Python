
# The while loops
# with the while loop we can execute a sset of statements as long as a condition is true.
# It is used when the number of iterations is not known.
# --> syntax.
#     while cond:
#        print() #prints it until the condition is true.



# Example1
i = 1
while i<6:
    print(f'{i}.hello world') 
    i+=1

# Example2
count = 1
while True:
    if count<6:
        print(count)
        count += 1
    else:
        break

# break statement
# break statement is used to exit the loop.
# anything after the break statement in a given loop will not be executed.

# Example
count = 0
while True:
    if count<10:
     count += 1
     print(f'5x{count}={5*count}')
    else:
        break

# continue statement
# The continue statement is used to skip at a given iterable.

# Example
count = 0
while count <= 20:
    if count % 2 != 0:
        count += 1
        continue
    print(count)
    count += 1
    
# The else statement
# With the else statement we can run a block of code once when the conditon no longer is true.
# -----SYNTAX-----
# while condition:
    # code to execute
# else:
    # code to execute if the loop condition becomes False


# Example
count = 0
while count <= 10:
    print(count)
    count += 1
else:
    print('the loop is completed')


# Example2 using break statements 
count = 0
while count < 5:
    if count == 3:
        break
    print(count)
    count += 1
else:
    print('the loop is completed!')
     
     

