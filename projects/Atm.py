class atm():
    def __init__(self,bankname,balance=500):
        self.bankname=bankname
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"deposited amount is :{amount}")
        print(f"after depositing your current balance is :{self.balance}")
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount 
            print(f"withdraw amount is {amount}")
            print(f"after withdrawing ,the amount is {self.balance}")
        else:
            print("insufficient balance")     
    def balance_enquiery(self):
        print(f"your current bank account balance is :{self.balance}") 

my_atm=atm("sbi")

while True:
    print("------atm menu-------")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.balance Enquiry")
    print("4.exit")
    choice=input("enter your choice:")
    if choice=="1":
        amount=int(input("enter the amount to deposit your account:"))
        my_atm.deposit(amount)
    elif choice=="2":
        amount=int(input("enter the withdraw amount:"))
        my_atm.withdraw(amount)
    elif choice=="3":
           my_atm.balance_enquiery() 
    elif choice=="4":
        print("thankyou and visit again ") 
        break
    else:
        print("invalid choice .choose the correct choice ")                

        
   
      
        