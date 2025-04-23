import math

class Shape:
    def __init__(self):
        self.shape = ""
        self.values = {}

    def accept_data(self):
        self.shape = input("Enter shape (square/rectangle/circle): ").lower()

        if self.shape == "square":
            self.values['side'] = float(input("Enter side: "))
        elif self.shape == "rectangle":
            self.values['length'] = float(input("Enter length: "))
            self.values['breadth'] = float(input("Enter breadth: "))
        elif self.shape == "circle":
            self.values['radius'] = float(input("Enter radius: "))
        else:
            print("Shape not supported")

    def area(self):
        if self.shape == "square":
            s = self.values['side']
            return s * s
        elif self.shape == "rectangle":
            l = self.values['length']
            b = self.values['breadth']
            return l * b
        elif self.shape == "circle":
            r = self.values['radius']
            return math.pi * r * r

    def perimeter(self):
        if self.shape == "square":
            s = self.values['side']
            return 4 * s
        elif self.shape == "rectangle":
            l = self.values['length']
            b = self.values['breadth']
            return 2 * (l + b)
        elif self.shape == "circle":
            r = self.values['radius']
            return 2 * math.pi * r

s = Shape()
s.accept_data()
print("Area:", s.area())
print("Perimeter/Circumference:", s.perimeter())
