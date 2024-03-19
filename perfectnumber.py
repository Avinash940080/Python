def is_perfect_number(num):
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num

number = int(input("Enter a number: "))
if is_perfect_number(number):
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")