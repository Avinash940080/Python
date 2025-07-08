# Arrays:

# Arrays are used to store multiple values in a single variable.
# We can use lists as arrays.

# Example:
car = ['volvo', 'BMW', 'mercedes']

# 2-D Arrays:
# 2d arrays are simply lists in list.

# Example-1:
car = ['volvo', 'BMW', 'mercedes']
bike = ['kawasaki', 'ducati', 'aprilia']

vehicle = [car, bike]
print(vehicle)


# Example-2:
# Taking the input from the user:
# We can only use this when we know the number of sublists in the main list.

car = list(map(str, input('enter the cars: ').split(',')))
bike = list(map(str, input('enter the bikes: ').split(',')))

vehicle = []

vehicle.append(car)
vehicle.append(bike)

print(vehicle)

# Example-3:
# We use while loop if we don't know the number of sublists in the main list.

scores = []

while True:
    student = {}
    names = input('enter the student name: ')
    marks = int(input('enter the marks of the student: '))
    student['name'] = names
    student['marks'] = marks
    scores.append(student)
    stop = input('enter ''stop'' to terminate: ')
    if stop.lower() == 'stop':
        break
    

print(f'scores: {scores}')
print(scores[0]['marks'])



