#Ask the user to enter a year. 
# Check whether it is a leap year using the standard leap year rules 
# (divisible by 4, but not by 100 unless also divisible by 400)
#  and display the result.

year=int(input("enter the year: "))

if year%4==0 and year%100!=0:
    print("Its a leap year")
elif year%400==0:
    print("its a leap year")
else:
    print("its not a leap year")
