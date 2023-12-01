# first and last digit of integer

def sum_first_last_digit(number):
    
    number = abs(number)
    last_digit = number % 10
    
    num_digits = len(str(number))
    
    first_digit = number // (10 ** (num_digits - 1))
    
    digit_sum = first_digit + last_digit
    
    return digit_sum

integer = 54879
result = sum_first_last_digit(integer)

print(f"The sum of the first and last digit of {integer} is: {result}")
