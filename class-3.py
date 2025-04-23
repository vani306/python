class Solid:
    def __init__(self):
        self.side = 0

    def accept_data(self):
        self.side = float(input("Enter side of the cube: "))

    def surface_area(self):
        return 6 * self.side * self.side

    def volume(self):
        return self.side ** 3

s = Solid()
s.accept_data()
print("Surface Area:", s.surface_area())
print("Volume:", s.volume())
