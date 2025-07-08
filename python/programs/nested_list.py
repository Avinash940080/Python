list1 = []

while True:
    sub_list = []
    while True:
        element = input('Enter the elements (separated by spaces). Type "done" if completed: ')
        if element.lower() == 'done':
            break
        sub_list.extend(element.split())
    list1.append(sub_list)
    another = input('Is there any sublists to enter? (yes/no): ')
    if another.lower() == 'no':
        break
print(list1)
