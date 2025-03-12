def student_data():
    return list(zip(*students))

students = [(101, "Kabir", 20), (102, "Vani", 19), (103, "Saumya", 18), (104, "Avani", 22)]

roll_nos, names, ages = student_data()

print("Roll Numbers:", list(roll_nos))
print("Names:", list(names))
print("Ages:", list(ages))
