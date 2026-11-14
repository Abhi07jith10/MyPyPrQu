employees = {
    101: {"name": "Abhi", "department": "IT", "salary": 60000},
    102: {"name": "Arun", "department": "HR", "salary": 45000},
    103: {"name": "Meera", "department": "Finance", "salary": 75000},
    104: {"name": "Anu", "department": "IT", "salary": 50000}
}

#1. Display the name and department of all employees

print({employees[i]["name"]:employees[i]["department"] for i in employees})

# 2. Find employees whose salary is greater than ■50,000.


print([employees[i]["name"] for i in employees if employees[i]["salary"]>50000 ])

# 3. Find the employee with the highest salary.
highest=0
for i in employees:
    if employees[i]["salary"]>highest:
        highest=employees[i]["salary"]
        char=employees[i]
print(char)

# 4. Calculate the average salary of all employees

new=[]

for i in employees:
    new.append(employees[i]["salary"])

total=sum(new)
avg=total/len(new)
print(avg)


