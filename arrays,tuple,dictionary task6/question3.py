#happy number

def is_happy_number(n):
    visited = set()
    while n != 1 and n not in visited:
        visited.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

given_list = [10, 501, 22, 37, 100, 999, 87, 351]

happy_numbers = [num for num in given_list if is_happy_number(num)]
count_happy_numbers = len(happy_numbers)

print("Count of happy numbers:", count_happy_numbers)
print("Happy numbers:", happy_numbers)
