length=int(input("enter length"))
breadth=int(input("enter breadth"))
area=length*breadth
perimeter=2*(length+breadth)
print("area is", area)
print("perimeter is", perimeter)
if area>perimeter:
    print("area is greater than perimeter")
else:
    print("area is not greater than perimeter")
