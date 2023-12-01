#prime number

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

given_list = [10, 501, 22, 37, 100, 999, 87, 351]

prime_numbers = [num for num in given_list if is_prime(num)]
count_prime = len(prime_numbers)

print("Count of prime numbers:", count_prime)
print("Prime numbers:", prime_numbers)
