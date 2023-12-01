#dupilcates lists

def find_duplicates(list1, list2, list3):
    
    combined_list = list1 + list2 + list3
    element_count = {}
    duplicates = []

    for element in combined_list:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    
    for element, count in element_count.items():
        if count > 1:
            duplicates.append(element)

    return duplicates

list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 3, 4, 7, 8]
list3 = [3, 4, 5, 9, 10]

result = find_duplicates(list1, list2, list3)
print("Duplicates:", result)

