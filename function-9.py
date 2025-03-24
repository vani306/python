def count_alpha_digits(s):
    result = {"alphabets": 0, "digits": 0}
    
    for char in s:
        if char.isalpha():
            result["alphabets"] += 1
        elif char.isdigit():
            result["digits"] += 1
    
    return result

text = input("Enter a string: ")
counts = count_alpha_digits(text)
print("Character counts:", counts)
