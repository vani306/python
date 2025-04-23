import csv

filename="students.csv"
data = [
    ["Roll no", "Name", "CP", "Maths", "Chemistry"],  
    ["102", "vani", "20", "21", "24"],
    ["103", "saumya", "20", "22", "25"],
    ["103", "avni", "19", "18", "20"],
    ["104", "neal", "20", "20", "21"]
]

with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{filename}' created successfully!")
