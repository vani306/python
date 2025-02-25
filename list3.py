import random

random_numbers = [random.randint(1, 30) for _ in range(50)]
print("Original List of Random Numbers:", random_numbers)

numbers = list(set(random_numbers))
print("List after removing duplicates:", numbers)
