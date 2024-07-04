import re
def validate_email(email):
    pattern = r'^[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    if re.fullmatch(pattern, email):
        return True
    else:
        return False

def validate_mobileno(mobile_no):
    pattern = r'^[7-9][0-9]{9}$'
    if re.fullmatch(pattern, mobile_no):
        return True
    else:
        return False

email = input("Enter an email: ")
mobile_no = input("Enter mobile number: ")

if validate_email(email):
    print("The email is valid")
else:
    print("The email is invalid")

if validate_mobileno(mobile_no):
    print("The mobile number is valid")
else:
    print("The mobile number is invalid")
