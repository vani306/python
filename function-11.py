def create_list(list1, list2):
    
    return list(set(list1) & set(list2))  

list1 = [1, 2, 3, 4, 5, 6]
print(list1)
list2 = [3, 4, 5, 6]
print(list2)
result = create_list(list1, list2)
print("Intersection of lists:", result)
