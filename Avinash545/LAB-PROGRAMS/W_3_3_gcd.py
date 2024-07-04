def gcd(a,b):
    while(a>0 and b>0):
        if(a>b): a= a%b
        else: b = b%a
    if(a==0): return b
    else: return a

a = int(input("Enter first number"))
b = int(input("Enter second number"))

print(gcd(a,b))