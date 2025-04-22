class Matrix:
    def __init__(self, m):
        self.m = m

    def add(self, other):
        return Matrix([[self.m[i][j] + other.m[i][j] for j in range(3)] for i in range(3)])

    def multiply(self, other):
        return Matrix([[sum(self.m[i][k] * other.m[k][j] for k in range(3)) for j in range(3)] for i in range(3)])

    def transpose(self):
        return Matrix([[self.m[j][i] for j in range(3)] for i in range(3)])

    def display(self):
        for row in self.m:
            print(row)

a= Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b= Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Addition: ")
a.add(b).display()

print("\nMultiplication: ")
a.multiply(b).display()

print("\nTranspose of first matrix: ")
a.transpose().display()
