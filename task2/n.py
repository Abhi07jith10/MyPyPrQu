#Take a number n from the user and print all numbers from 1 to n that are divisible by 7.
#Also find their sum using a while loop

n=int(input("Enter the number : "))

i=1
sum=0
while i<=n:
    if i%7==0:
        print(i)
        sum=sum+i
    i+=1
    
print(f"the sum is {sum}")










