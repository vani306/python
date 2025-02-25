import random 
random_numbers= {random.randint(15, 45) for _ in range(10)}
print(random_numbers)

count= sum(1 for num in random_numbers if num <30)
print("numbers less than 30: ", count)

random_numbers= {num for num in random_numbers if num <=35}
print("after removing numbers greater than 35:", random_numbers)


