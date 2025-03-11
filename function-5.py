def ispangram(input_string):
    input_string= input_string.replace(" ", "").lower()

    return set('abcdefghijklmnopqrstuvwxyz') <= set(input_string)

string1= "The quick brown fox jumps over the lazy dog"
string2= "Crazy Fredrick bought many very exquisite opal jewels"

print(ispangram(string1))
print(ispangram(string2))
