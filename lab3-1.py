#//print all alphabets in uppercase and lowercase
def main():
    print("alphabets from (A-Z) are:")
    for i in range(65,91):
       print(chr(i), end=" ")

    print("alphabets from (a-z) are:")
    for i in range(97,123):
       print(chr(i), end=" ")
main()
