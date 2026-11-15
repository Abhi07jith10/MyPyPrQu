employees = {
 101: {"salary": 25000},
 102: {"salary": 45000},
 103: {"salary": 65000},
 104: {"salary": 50000}
}

highest=0
for i in employees:
    if employees[i]["salary"]>highest:
        highest=employees[i]["salary"]
        char=i

print(char,highest)