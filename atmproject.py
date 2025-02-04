balance=500

def deposit(amount):
    global balance
    balance+=amount
    print(f"deposited balance:Rs{balance}")
    
def withdraw(amount):
    global balance
    if balance>=amount:
        balance-=amount 
        print(f"withdraw amount is {amount}")
        print(f"after withdrawing ,the amount is {balance}")
    else:
        print("insufficient balance")     




def balance_enquiery():
    print(f"available balance in your account is :{balance}")
print(balance_enquiery())  

while True:
    print("------atm menu-------")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.balance Enquiry")
    print("4.exit")
    choice=input("enter your choice:")
    if choice=="1":
        amount=int(input("enter the amount to deposit your account:"))
        deposit(amount)
    elif choice=="2":
        amount=int(input("enter the withdraw amount:"))
        withdraw(amount)
    elif choice=="3":
           balance_enquiery() 
    elif choice=="4":
        print("thankyou and visit again ") 
        break
    else:
        print("invalid choice .choose the correct choice ")      
    

