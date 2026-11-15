#  Student Mark Analysis
# Display each student's name, total marks, average marks and result. A student passes only if they score at least 40 in
# every subject.
# students = {
#  101: {"name": "Arun", "marks": [80, 75, 90]},
#  102: {"name": "Meera", "marks": [35, 60, 70]},
#  103: {"name": "Rahul", "marks": [90, 85, 95]}
# }
# Expected output:
# Arun - Total: 245, Average: 81.67, Pass
# Meera - Total: 165, Average: 55.00, Fail
# Rahul - Total: 270, Average: 90.00, Pass


students = {
  101: {"name": "Arun", "marks": [80, 75, 90]},
  102: {"name": "Meera", "marks": [35, 60, 70]},
  103: {"name": "Rahul", "marks": [90, 85, 95]}
 }

for i in students:
    total=sum(students[i]["marks"])
    avg=total//3
    if students[i]["marks"][0]>40 and students[i]["marks"][1]>40 and students[i]["marks"][2]>40:
        print(f"{students[i]["name"]}:Total:{total},average:{avg}, pass")
    else:
        print(f"{students[i]["name"]}:Total:{total},average:{avg}, fail")

