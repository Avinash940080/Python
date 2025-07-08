# Python provides several types of conditional statements:
'''
1. if statement
2. if-else statement
3. if-elif-else statement

'''

'''
Some of the logical conditions used are
a == b
a != b
a < b
a <= b
a > b
a >= b

''' 


#1  if statement
#   The if statement is used to test a condition. If the condition is True, the code block under block the if statement is executed.
# Syntax used is "if condition:"
#                   print(content executed if it is true) 


# Example
a = 10
b = 20

if a != b:
    print('not equal')

a = 10
b = 20

if a < b:
    print("b is greater than a")



#2 if-else statement:
#  if-else statement allows you to execute one block of code when the condition is True, and another block of code when the is False.
#  Syntax -->
'''
if condition:
   print() #prints if the condition is true.
else:
   print() #prints if the condition is not true

'''

# Example

a = 10
b = 20

if a == b:
    print('a is equal to b')
else:
    print('a is not equal to b')

#3.if-elif-else statement:
#  if-elif-else statement allows you to test multiple conditions, The first block of code where the condition is True gets executed.
'''
---SYNTAX---

if cond1:
    print() #prints if cond1 is true else goto next step
elif cond2:
    print() #prints if cond2 if true else next step
else:
    print() #prints if doesnot folow any of the conditions

'''

# Example

score =int(input('enter your score'))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print('Grade: B')
elif score >= 70:
    print('Grade: C')
elif score >= 60:
    print('Grade: D')
else:
    print('fail')




# Nested if Statements
# You can nest if statements inside other if statements for more complex conditions.

'''
------SYNTAX-------

if condition1:
    if condition1.1: #falls to this condition if condition1 is true
       print()
    else:
       print()
else:                #if doesnot follows the cond1 then it is printed
    print()
'''

# Example:
AGE = int(input('Enter your AGE:'))
citizenship = str(input('enter yes or no if you are a citizen.'))

if AGE >= 18:
    if citizenship == 'yes':
        print('you are eligible to vote')
    else:
        print('You must be a citizen to vote')
else:
    print('You are not old enough to vote')


# Short hand if-else statements:
# This helps in keeping your simple and readable.
# Syntax--> value_if_true if condition else value_if_false

# Example

number = int(input('Enter the number:'))

print('Even') if number%2 == 0 else print('odd')



# Logical operators can also be used in this condition statements.
'''
and  #example - a > b and a < b
or  #example -  a > b or a < b
not #example -  a > b not a < b

'''