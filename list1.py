import random
Lodd=[]
for i in range(5):
    Lodd.append(random.randrange(0,200) * 2 -1)
print(Lodd)
Leven=[]
for i in range(4):
    Leven.append(random.randrange(0,200) * 2)
print(Leven)

Lodd.pop(2)
print(Lodd)

Lodd.insert(2,Leven)
print(Lodd)
    
Lodd.concatenate()
print(Lodd)

lodd.sort()
print(Lodd)
