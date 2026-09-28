#Write a program to print all numbers between 1 and 100 that are divisible by both 3
#and 5 using a while loop

i=1

while i<=100:
    if i%3==0 and i%5==0:
        print(i)
    i+=1



