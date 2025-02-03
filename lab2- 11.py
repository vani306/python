#//given three points, check if all three points fall on one straight line
def are_points_collinear(x1, y1, x2, y2, x3, y3):
    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    return area == 0

x1, y1 = 1, 2
x2, y2 = 2, 3
x3, y3 = 3, 4

if are_points_collinear(x1, y1, x2, y2, x3, y3):
    print("The points are collinear")
else:
    print("The points are not collinear")
