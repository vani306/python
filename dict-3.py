
employees = [
    (120, 10, 50000), (121, 11, 70000), (122, 12, 60000),
    (120, 13, 75000), (122, 14, 48000), (121, 15, 82000)
]

dept_salaries = {}
for dept, _, salary in employees:
    dept_salaries.setdefault(dept, []).append(salary)

for dept, salaries in dept_salaries.items():
    print(f"Department {dept}: Min Salary = {min(salaries)}, Max Salary = {max(salaries)}")

