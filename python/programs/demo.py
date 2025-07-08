print('hello world')
list1 = []



while True:
    sub_list = []
    while True:
        element = input('enter the elements. enter done if completed: ')
        if element.lower() == 'done':
            break
        sub_list = element.split()
    list1.append(sub_list)
    another = input('is there any sublists to enter: (yes/no)')
    if another.lower() == 'no':
     break
print(list1)