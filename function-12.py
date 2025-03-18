
def prime_factors(n, divisor=2):
    if n ==1:
        return []
    elif n%divisor ==0:
        return [divisor]+ prime_factors(n// divisor, divisor)
    else:
        return prime_factors(n, divisor + 1)
num= int(input("enter a positive integer: "))
print("prime factors: ", prime_factors(num))
