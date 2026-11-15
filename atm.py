#create a class ATM
#method 1 (details, balance=10000, name)
#method2 = deposit()
#method3 = withdrawl()
#method4 = check balance


# Hy Abhi welcome to SBI BANK
# Hy your deposit is succesfull
# Your account balance after deposit is 12000
# withdrawl succesfull
# Your account balance after withdrawl is 7000
# Your balance amount is 7000

class Atm():
    def details(self,name,balance):
        self.name=name
        self.balance=balance
        print(f"Hy {name} welcome to SBI bank. ")
        print(F"your current balance is {balance}")

    def deposit(self,deposit_amount):
        
        self.balance+=deposit_amount
        print("Deposit sucessfull")
        

    def withdrawl(self,withdrawl_amount):
        self.balance-=withdrawl_amount
        print("Withdrawl sucessfull")
    def check_balance(self):
        
        print(f"Your balance is {self.balance}")

obj1=Atm()
obj1.details("Abhi",10000)
obj1.deposit(2000)
obj1.withdrawl(5000)
obj1.check_balance()
