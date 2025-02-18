# Python program to find all Pythagorean

def pythagoreanTriplets(limit):

    ans = []

    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            for c in range(b, limit + 1):
                if a * a + b * b == c * c:
                    ans.append([a, b, c])

    return ans

limit = 30
ans = pythagoreanTriplets(limit)

for triplet in ans:
    for num in triplet:
        print(num, end=" ")
    print()
