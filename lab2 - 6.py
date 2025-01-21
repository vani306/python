#//accept a number from user and print number of digits in it
n=int(input("enter a number"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("number of digits are", count)   
