# fibonacci series
# 0,1,1,2,3,5,8,...

fib = []
n = int(input('enter no.of terms: '))
a, b = 0, 1

for i in range(n):
    fib.append(a)
    a, b = b, a+b
    i += 1
print(fib)
    

# Prime numbers in a given range
n1 = int(input(''))
n2 = int(input(''))
list1 = []

for i in range(n1, n2+1):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count += 1
    if count <= 2:
        list1.append(i)
print(list1)



n = int(input())
sum = 0
for i in range(1,n+1):
    sum += i
    i += 1

print(sum)