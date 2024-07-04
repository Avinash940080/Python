def palindrome(str):
    for i in range(0,len(str)):
        if(str[i]!= str[len(str)-i-1]):
            return False
            break;
    return True

str = input("Enter the string")
print(len(str))
if(palindrome(str)==True):
    print("Given string is palindrome")
else:
    print("It is not palindrome")