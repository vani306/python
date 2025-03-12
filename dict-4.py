text = input("Enter a string: ")
char_freq = {char: text.count(char) for char in set(text)}
print("Character Frequency:", char_freq)
