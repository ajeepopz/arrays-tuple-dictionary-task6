#minimum elements in a rated and sorted lists

def find_minimum_element(sorted_list):
    if not sorted_list:
        return None  
    return sorted_list[0]  

ratings = [1, 2, 3, 4, 5]
minimum_rating = find_minimum_element(ratings)

if minimum_rating is not None:
    print(f"The minimum rated element is: {minimum_rating}")
else:
    print("no minimum rated elements")

