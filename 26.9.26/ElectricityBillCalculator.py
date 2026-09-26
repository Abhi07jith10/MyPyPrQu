#Ask the user to enter units of electricity consumed. 
# If units ≤ 100, rate is ₹5/unit. 
# If units are 101–200, rate is ₹7/unit. 
# If units are above 200, rate is ₹10/unit. 
# Calculate and display the total bill.

units=int(input("enter the units of electricity consumed: "))

if units<=100:
    total_bill=units*5
    print(f"The total bill for the consumed electricity per unit is {total_bill} ")
elif units>=101 and units<=200:
    total_bill=units*7
    print(f"The total bill for the consumed electricity per unit is {total_bill} ")
    
elif units>200:
    total_bill=units*10
    print(f"The total bill for the consumed electricity per unit is {total_bill} ")
else:
    print("Invalid input")


