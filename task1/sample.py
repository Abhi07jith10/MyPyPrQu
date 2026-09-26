#Create four variables — one each of type str, int, float, and bool — 
# for a student's name, roll number, CGPA, and pass/fail status. 
# Print each variable along with its type using type().

name=input("enter the name: ")
rollno=int(input("enter the roll no: "))
cgpa=float(input("enter the cgpa: "))
status=cgpa > 5.0

print(f"name is {name} and its type is {type(name)}")

print(f"roll no is {rollno} and its type is {type(name)}")

print(f"cgpa is {cgpa} and is type is {type(cgpa)}")

print(f"status is {status} and its type is {type(status)}")

