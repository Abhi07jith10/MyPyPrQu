#Ask the user to enter two numbers and an operator (+, -, *, /). 
# Use if-elif-else to perform the corresponding operation and display the result. 
# If the operator is invalid, display "Invalid operator". 
# Handle division by zero separately.

num1=int(input("enter the first number :"))
num2=int(input("enter the second number :"))

print ("enter any of the following operators (+,-,*,/)")
operator=input("enter the operator: ")

if operator=="+":
    output=num1+num2
    print(f"output of the specific operation is {output}")
elif operator=="-":
    output=num1-num2
    print(f"output of the specific operation is {output}")
elif operator=="*":
    output=num1*num2
    print(f"output of the specific operation is {output}")
elif operator=="/":
    output=num1/num2
    print(f"output of the specific operation is {output}")
else:
    print("invalid operator")
    

