import random

def generate_random_numbers(n=30, range_min=-100, range_max=100):
    
    return [random.randint(range_min, range_max) for _ in range(n)]

random_numbers = generate_random_numbers()

positive_numbers = [num for num in random_numbers if num > 0]
negative_numbers = [num for num in random_numbers if num < 0]

print("Random Numbers:", random_numbers)
print("Positive Numbers:", positive_numbers)
print("Negative Numbers:", negative_numbers)
