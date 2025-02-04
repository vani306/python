#//count no. of alphabets and no. of digits in any given string
string=input("enter a string")
alphabets=digits=0
for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets=alphabets+1

for i in range(len(string)):
    if(string[i].isdigit()):
        digits=digits+1

print("alphabets in string are:", alphabets)
print("digits in string are:", digits)
        
