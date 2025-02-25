
def remove_substring(str1, str2):
    if str2 in str1:
        str1 = str1.replace(str2, "")
    return str1

string1 = input("Enter the first string: ")
string2 = input("Enter the string to remove: ")

print(remove_substring(string1, string2))
