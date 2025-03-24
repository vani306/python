def convert(s):
    words = s.split()  
    unique_words = set(words)  
    sorted_words = sorted(unique_words)  
    return ' '.join(sorted_words)  

text = input("Enter a string: ")
result = convert(text)
print("Processed string:", result)
