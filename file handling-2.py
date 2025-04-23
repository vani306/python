import csv

data = {}
with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        roll_no = int(row['Roll no'])
        total = int(row['CP']) + int(row['Maths']) + int(row['Chemistry'])
        data[roll_no] = {
            'Name': row['Name'],
            'Marks': [int(row['CP']), int(row['Maths']), int(row['Chemistry'])],
            'Total': total
        }

for k, v in data.items():
    print(f"Roll no: {k}, Name: {v['Name']}, Total: {v['Total']}")
    

        
            
