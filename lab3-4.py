def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

def is_perfect(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    sum_of_powers = sum(int(digit) ** power for digit in num_str)
    return sum_of_powers == n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    square = n ** 2
    return str(square).endswith(str(n))

# Example usage:
number = int(input("Enter a number: "))

print(f"Is {number} prime? {'Yes' if is_prime(number) else 'No'}")
print(f"Is {number} perfect? {'Yes' if is_perfect(number) else 'No'}")
print(f"Is {number} Armstrong? {'Yes' if is_armstrong(number) else 'No'}")
print(f"Is {number} palindrome? {'Yes' if is_palindrome(number) else 'No'}")
print(f"Is {number} automorphic? {'Yes' if is_automorphic(number) else 'No'}")
