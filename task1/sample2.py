# Write a program that takes two numbers as input and prints their sum. 
# Run it and check — does it add the numbers, or does it concatenate them?
# Fix it so it actually adds them.

num1=input("enter the number :")
num2=input("enter the number :")
sum=num1+num2
print(sum)

#The above line of code just treats the number we are giving as string
#forex.if we give 1 and 2 as two numbers instead of giving output as 3 
#we will get op as 12 (concatenate)

num1=int(input("enter the number :"))
num2=int(input("enter the number :"))
sum=num1+num2
print(sum)

#here the op will be 3 since the numbers are treated as integers and not strings

