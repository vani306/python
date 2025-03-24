def is_palindrome(s):
    cleaned_s = ''.join(s.split()).lower()  
    return cleaned_s == cleaned_s[::-1]  


text = input("Enter a string: ")
if is_palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
