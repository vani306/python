#//check the point_in_circle
x=int(input("enter the value"))
x1=int(input("enter the value"))
y=int(input("enter the value"))
y1=int(input("enter the value"))
r=int(input("enter the value"))

distance_squared = (x - x1)**2 + (y - y1)**2
radius_squared = r**2
    
if distance_squared < radius_squared:
    print("The point is inside the circle")
elif distance_squared == radius_squared:
    print("The point is on the circle")
else:
    print("The point is outside the circle")

