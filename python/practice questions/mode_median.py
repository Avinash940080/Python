# Mode - most repeated value of the data.
# median - middle most value of a sorted dataset.

def calc_mode(numbers):
    frequency_dict = {}
    for value in numbers:
        if value in frequency_dict:
            frequency_dict[value] += 1
        else:
            frequency_dict[value] = 1
    
    max_frequency = 0
    for value in frequency_dict.values():
        if value > max_frequency:
            max_frequency = value
        
    modes = []
    for key, value in frequency_dict.items():
        if value == max_frequency:
         modes.append(key)
    for x in modes:
        return x
    
def calc_median(numbers):
     numbers.sort()
     num = len(numbers)
     middle = num // 2
     if num%2 == 0:
        middle = numbers//2
        median = (numbers[middle]+numbers[middle-1])/2
     else:
        median = numbers[middle]
     return median

scores = list(map(int, input().split(',')))
mode = calc_mode(scores)
print(f'Mode: {mode}')
median = calc_median(scores)
print(f'Median: {median:.2f}')
            
        
    
