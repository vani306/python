def dectobin(n,d=2):
    ans = " "
    while n != 0:
        r = n%d
        ans = str(r)+ans
        #print(r,end=")
        n = n//d
    print(ans)
dectobin(25)

def dectobinrec(n,d=2):
    r = n%d
    if n:
        dectobinrec(n//d)
    print(r,end=" ")

print()
dectobinrec(25)          
