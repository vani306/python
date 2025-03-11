def tuples(end_value):
    return [(x, x**2, x**3) for x in range(1, end_value + 1)]

end_value= 5
result= tuples(end_value)

for i in result:
    print(i)
