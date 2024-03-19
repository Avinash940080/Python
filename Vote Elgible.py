def is_eligible_for_vote(age):
    if age >= 18:
        return True
    else:
        return False

age = int(input("Enter your age: "))
if is_eligible_for_vote(age):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")