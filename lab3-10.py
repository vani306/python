# Function to print first N natural numbers in reverse
def reverse(n):
    for i in range(n, 0, -1):
        print(i, end=" ")

n = 10
reverse(n)
