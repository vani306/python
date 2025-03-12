def separate_names(names_set):
    
    a_names = {name for name in names_set if name.startswith('A')}
    b_names = {name for name in names_set if name.startswith('B')}
    
    return a_names, b_names

names = {"Avani", "Beena", "Ankita", "Bhavya", "Ayaan", "Bani"}

a_names, b_names = separate_names(names)
print("Names starting with A:", a_names)
print("Names starting with B:", b_names)
