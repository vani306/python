class Box:
    def __init__(self):
        self.height = 0
    def input_height(self):
        self.height = float(input("enter height:"))

class Box1(Box):
    def __init__(self):
        super().__init__()
        self.length = 0
        self.breadth = 0

    def input_length_breadth(self):
        self.length = float(input("enter length: "))
        self.breadth= float(input("enter breadth: "))

    def volume(self):
        return self.length*self.breadth*self.height

box=Box1()
box.input_height()
box.input_length_breadth()
print("volume of box is :", box.volume())
