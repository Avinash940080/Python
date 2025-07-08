# Complex grading using nested if elif else statements

score = int(input('enter your score = '))

if score > 100:
    print('Invalid score. Score cannot be above 100')
else:
    if score >= 90:
        Grade = 'A'
        print(f'Your Grade is: {Grade}')
    elif score >= 80:
        Grade = 'B'
        print(f'Your Grade is: {Grade}')
    elif score >= 70:
        Grade = 'C'
        print(f'Your Grade is: {Grade}')
    elif score >= 60:
        Grade = 'D'
        print(f'Your Grade is: {Grade}')
    else:
        Grade = 'F'
        print(f'Your Grade is: {Grade}')
    




