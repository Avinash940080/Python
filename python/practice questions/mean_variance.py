# mean and variance of a given sample population:

def avg_mean(numbers):
    total_sum = 0
    for x in numbers:
        total_sum += x
    sum = total_sum
    num = len(numbers)
    avg = sum/num
    return avg
def var_num(numbers):
    mean = avg_mean(numbers)
    n = len(numbers)

    sum_of_squared_differences = 0
    for x in numbers:
        difference = x-mean
        squared_difference = difference**2
        sum_of_squared_differences += squared_difference
    var = sum_of_squared_differences/(n-1)
    return var




sales = list(map(int, input('enter the sales with comma: ').split(',')))
mean = avg_mean(sales)
variance = var_num(sales)
print(f'Mean: {mean:.2f}')
print(f'Variance: {variance:.2f}')
