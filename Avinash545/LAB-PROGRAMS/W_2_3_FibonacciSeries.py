n = int(input("Enter the number : " ))
a = 0
b = 1
c = 0
if n<=0:
    print("Enter positive number : ")
elif n==1:
    print(a)
else:
    print("Fibnonacci series : ",end=" ")
    print(a,end= " ")
    print(b,end=" ")
    while(c<n):
        c = a+b
        print(c,end =" ")
        a=b
        b=c
