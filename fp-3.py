import random

random_numbers = random.sample(range(-15, 15), 10)

squared_numbers = [x ** 2 for x in random_numbers]

print("Random numbers: ",random_numbers)
print("Squared numbers: ",squared_numbers)
