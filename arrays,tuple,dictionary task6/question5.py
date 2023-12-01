#minimum and maximum of students

def distribute_mangoes(mangoes, students):
    mangoes.sort()  
    min_difference = float('inf')  
    num_bags = len(mangoes)
    
    if num_bags < students:
        return -1
    
    for i in range(num_bags - students + 1):
        min_difference = min(min_difference, mangoes[i + students - 1] - mangoes[i])
    
    return min_difference


bags = [7, 3, 2, 4, 1,9, 12, 56]
num_students = 3

result = distribute_mangoes(bags, num_students)
print(f"The minimum difference in mangoes distributed is: {result}")
