#Ask the user to enter a number. 
# Check and display whether it is positive, negative, or zero, and also whether it is even or odd.

num=int(input("enter the number : "))

if num>0:
    if num%2==0:
        print("The number is a positive and a even number.")
    else:
        print("The number is a positive and a odd number.")

elif num<0:
    if num%2==0:
            
            print("The number is a negative and a even number.")
    else:
            print("The number is a negative and a odd number.")
else:
     print("the number is zero")
     