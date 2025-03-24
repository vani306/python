def frequency(s):
    
    words = s.split()  # Split the string into words
    freq_dict = {}
    
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1  # Count word occurrences
    
    sorted_freq = dict(sorted(freq_dict.items()))  # Sort dictionary by word
    return sorted_freq

text = input("Enter a string: ")
word_counts = frequency(text)
print("Word frequencies:", word_counts)
