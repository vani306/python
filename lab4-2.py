a = "Hello World"
print(a.lower())


a = "Hello World"
print(a.upper())


def toggle_case(string):
    return ''.join([char.lower() if char.isupper() else char.upper() for char in string])

string = "Hello World!"
print(toggle_case(string))

