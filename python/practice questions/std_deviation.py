# Standard deviation for a sample variance
def avg(numbers):
    sum = 0
    n = len(numbers)
    for x in numbers:
        sum += x
    mean = sum/n
    return mean

def var(numbers, mean):
    num = len(numbers)
    
    sum_sqrd_diff = 0
    for x in numbers:
        diff = x-mean
        sqrd_diff = diff**2
        sum_sqrd_diff += sqrd_diff
    variance = sum_sqrd_diff/(num -1) 
    return variance

def std_dev(numbers):
    mean = avg(numbers)
    variance = var(numbers, mean)
    standard_deviation = variance**0.5
    return standard_deviation
    
numbers = list(map(float, input().split(',')))
standard_deviation = std_dev(numbers)
print(f'Standard Deviation: {standard_deviation:.2f}')
