def count_vowels(v):
    if not v:
        return 0

    if v[0].lower() in 'aeiou':
        return 1 + count_vowels(v[1:])
    else:
        return count_vowels(v[1:])
    
str= input("enter a string: ")
count_vowels(str)
print(f"number of vowels in the string is : {count_vowels(str)}")
