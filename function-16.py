def power(a=1, b=0):
    if b == 0:
        return 1
    return a * power(a=a, b=b-1)

print("Result:", power(a=2, b=3))  
