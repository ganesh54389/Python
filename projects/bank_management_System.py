class bankAccount:
    def __init__(self,account_holder,balance=0.0):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"deposited amount is :{amount},after depositing the amount is {self.balance}")
        else:
            print("invalid deposited amount") 
    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            print(f"the withdraw amount is {amount} ,aftee withdrawing the amount is {self.balance}")
        else:
            print("invalid withdraw fund")
    def check_balance(self):
        print(f"account balance is {self.account_holder}:Rs{self.balance}")



class bankManagementSystem:
    def __init__(self):
        self.account={  }
    def create_account(self,account_holder,initial_balance=0.0):
        if account_holder not in self.account:
            self.account[account_holder]=bankAccount(account_holder,initial_balance) 
            print("account created succsesfully")
        else:
            print("account already exists")
    def get_account(self,account_holder):
        return self.account.get(account_holder,None)
    def deposit(self,account_holder,amount):
        account=self.get_account(account_holder)
        if account:
            account.deposit(amount)
        else:
            print("account not found")    
    def withdraw(self,account_holder,amount):
        account=self.get_account(account_holder)
        if account:
            account.withdraw(amount)      
        else:
            print("account not found")  
    def check_balance(self,account_holder):
        account=self.get_account(account_holder)
        if account:
            account.check_balance()
        else:
            print("account not found")


bank=bankManagementSystem()
while True:
    print("welcome to the bank management System")
    print("1.create a account")
    print("2.deposit")
    print("3.withdraw")
    print("4.check balance")
    print("5.exit")

    choice=input("enter your choice :")
    if choice=="1":
        account_holder=input("enter the account holder name :")
        initial_balance=float(input("enter the initial balance:"))
        bank.create_account(account_holder,initial_balance)
    elif choice=="2":
        account_holder=input("enter the account holder name :")
        amount=float(input("enter the initial balance:"))
        bank.deposit(account_holder,amount)
    elif choice=="3":
        account_holder= input("enter the account holder name :") 
        amount=float(input("enter the initial balance:"))
        bank.withdraw(account_holder,amount)  
    elif choice=="4":
        account_holder= input("enter the account holder name :") 
        bank.check_balance(account_holder)  
    elif choice=="5":
        print("thank you for visiting our bank")
        break
    else:
        print("invalid choice please provide valid choice")    




   
     
        