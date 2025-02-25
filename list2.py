import random
random_integers = [random.randint(1, 15) for _ in range(20)]
print(random_integers)

x=int(input("enter number from random_integers"))

indices = []
for i in range(len(random_integers)):
    if random_integers[i] == x:
        indices.append(i)

print(indices)
