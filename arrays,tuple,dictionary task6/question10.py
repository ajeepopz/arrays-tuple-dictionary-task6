#sum of equal to zero

def zero(nums):
    prefix_sums = set()
    current_sum = 0

    for num in nums:
        current_sum += num
        if current_sum in prefix_sums or current_sum == 0:
            return True

        prefix_sums.add(current_sum)

    return False
given_list = [4, 2, 3, 1, 6,]
result = zero(given_list)

if result:
    print("There is a sublist with a sum equal to zero.")
else:
    print("No sublist with a sum equal to zero.")
