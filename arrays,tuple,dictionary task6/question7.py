#non-repeating elements

def non_repeating_element(nums):
    count_dict = {}
    
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    for num in nums:
        if count_dict[num] == 1:
            return num
    return None 

numbers = [4, 6, 2, 4, 3, 2, 1, 5, 5]
result = non_repeating_element(numbers)

if result is not None:
    print(f"The first non-repeating element is: {result}")
