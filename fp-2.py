
list1 = [1, 2, 2, 4, 5, 6]
list2 = [4, 5, 4, 0, 3, 3]

result = list(map(lambda x, y: x + y, list1, list2))

print(result)
