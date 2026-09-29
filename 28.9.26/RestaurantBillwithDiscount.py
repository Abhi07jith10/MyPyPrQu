#Ask the user to enter their total bill amount. 
# If the bill is above ₹2000, apply a 10% discount. 
# If it's between ₹1000 and ₹2000, apply a 5% discount. 
# Otherwise, no discount. Display the final amount to pay.

Bill_amount= int(input("enter the total bill amount : "))
discount=0

if Bill_amount>2000:
    discount=0.1
elif Bill_amount>=1000 and Bill_amount<=2000:
    discount= 0.05
else:
    print("There is no discount therefore the ")

discount_Rate=Bill_amount*discount
final_bill=Bill_amount-discount_Rate
print(f"The final bill amount is {final_bill}")

