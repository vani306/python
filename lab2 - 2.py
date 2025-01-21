#//print largest and smallest values out of three
a=int(input("enter first value"))
b=int(input("enter second value"))
c=int(input("enter third value"))
if a>b & a>c:
    print("largest value out of three is", a)
elif b>c & b>a:
    print("largest value out of three is", b)
else :
    print("largest value out of three is", c)
if a<b & a<c:
    print("smallest value out of three is", a)
elif b<a & b<c:
    print("smallest value out of three is", b)
else :
    print("smallest value out of three is", c)
