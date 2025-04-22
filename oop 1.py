class Box :
    def __init__(self):
        self.length=0
        self.breadth=0
        self.height=0

    def input_area(self):
        self.length= float(input("Enter length:"))
        self.breadth= float(input("Enter breadth:"))
        
    def input_volume(self):
        self.length= float(input("Enter length:"))
        self.breadth= float(input("Enter breadth:"))
        self.height= float(input("Enter height:"))

    def area(self):
        return self.length*self.breadth

    def volume(self):
        return self.length*self.breadth*self.height
box = Box()
    
box.input_area()
print("Area of box is :", box.area())

box.input_volume()
print("Volume of box is :", box.volume())
