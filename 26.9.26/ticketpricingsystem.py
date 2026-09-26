#Ask the user for their age. If age is below 5, ticket is free. 
# If age is between 5 and 12, ticket costs ₹100.
# If age is between 13 and 60, ticket costs ₹250. 
# If age is above 60, ticket costs ₹150 (senior discount). 
# Display the applicable ticket price.

age=int(input("enter the age: "))


if age<5:
    print("Ticket is free")
elif age>=5 and age<=12:
    print("The ticket costs 100 rupees")
elif age>=13 and age<=60:
    print("The ticket costs 250 rupees")
elif age>60 :
    print("The ticket costs 150 rupees")
else:
    print("invalid input")


