import numbers
def min(numbers):
    result = numbers[0]
    for num in numbers:
        if result > num:
            result = num
    return result
min_number = min(numbers)
print("Min number: ", min_number)