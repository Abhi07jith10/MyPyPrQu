# Employee Salary Analysis
# Calculate the total salary expenditure of each department and identify the employee receiving the highest salary.
# employees = {
#  101: {"name": "Arun", "department": "Python", "salary": 30000},
#  102: {"name": "Meera", "department": "Data Science", "salary": 45000},
#  103: {"name": "Rahul", "department": "Python", "salary": 35000},
#  104: {"name": "Anu", "department": "Data Science", "salary": 40000}
# }
# Expected output:
# Python: 65000
# Data Science: 85000
# Highest Salary: Meera - 45000

employees = {
  101: {"name": "Arun", "department": "Python", "salary": 30000},
  102: {"name": "Meera", "department": "Data Science", "salary": 45000},
  103: {"name": "Rahul", "department": "Python", "salary": 35000},
  104: {"name": "Anu", "department": "Data Science", "salary": 40000}
 }

python_total=0
DS_total=0

for i in employees:
    if employees[i]["department"]=="Python":
        python_total+=employees[i]["salary"]
    elif employees[i]["department"]=="Data Science":
            DS_total+=employees[i]["salary"]

highest_salary=0
top_name=""
for j in employees:
     if employees[j]["salary"]>highest_salary:
              highest_salary=employees[j]["salary"] 
              top_name=employees[j]["name"]


print(f"Python: {python_total}")
print(f"Data Science: {DS_total}")
print(f"Highest salary : {top_name}, salary : {highest_salary}")



