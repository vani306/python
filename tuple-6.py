my_tuple = (1, 2, 3, 4, 5)

temp_list = list(my_tuple)
temp_list[2] = 10

my_tuple = tuple(temp_list)

print(my_tuple)
