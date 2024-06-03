def sum_of_digits(number):
    sum_digits = 0
    for digit in str(number):
        sum_digits += int(digit)
    return sum_digits

def max_sum_of_digits(numbers):
    max_number = None
    max_sum = -1
    for number in numbers:
        current_sum = sum_of_digits(number)
        if current_sum > max_sum:
            max_sum = current_sum
            max_number = number
    return max_number
