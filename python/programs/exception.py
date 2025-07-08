# -----------------------------------> Exception Handling: <-----------------------------------------


# When an error occurs, or exception as we call it, Python will normally stop stop and generate an error message.
# These exceptions can be handled using the 'try' statement.

# Example:
x = input()
try:
    print(int(x))
except:
    print("Please give a valid input!")


# ----------------> Many Exceptions:
# You can define as many exception blocks as you want, 
# ex: if you want execute a special block of code for a special kind of error.

# Example:
x = int(input())

try:
    print(int(100/x))
except NameError:
    print('Variable x is not defined')
except ArithmeticError:
    print('zero division error')
except:
    print()
except:
    print("Something else not went wrong")