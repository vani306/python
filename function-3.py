def create_array(x,y,z,init_value):

    return[[[init_value for _ in range(z)] for _ in range(y)] for _ in range(x)]
x,y,z=3,4,5
n=7
array=create_array(x,y,z,n)

for layer in array:
    for row in layer:
        print(row)
    print()     
