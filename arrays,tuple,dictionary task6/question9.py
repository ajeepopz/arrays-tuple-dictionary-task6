#sort the list value with 59

def triplet_with_sum(nums, target_sum):
    n = len(nums)

    
    nums.sort()
    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target_sum:
                return [nums[i], nums[left], nums[right]]
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

    return None
given_list = [10, 20, 30, 9]
target_value = 59

triplet = triplet_with_sum(given_list, target_value)

if triplet:
    print(f"The triplet with sum {target_value} is: {triplet}")
else: 
    print("No triplet found with the given sum.")



