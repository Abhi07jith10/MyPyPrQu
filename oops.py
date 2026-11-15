#create a class 
#method 1 :accept a string and return the count of each character in the string
#method 2 :accept a  number and check the number is prime or not
#method 3 :accept a list of numbers and return the sum of even numbers from the list.


class problem():
    def count(self,word):
        new=''
        for i in word:
            if i not in new:
                new+=i
                print(f"{i}:{word.count(i)}")

    def is_prime(self,number):
        for i in range(2,number):
            if number%i==0:
                print("not prime")
                break
        else:
            print("prime")
    def even_sum(self,numbers):
        even=list(filter(lambda a:a%2==0,numbers))
        print(sum(even))

obj1=problem()
obj1.count("hello")
obj1.is_prime(11)
obj1.even_sum([1,2,3,4,5,6,7,8,9,10])

