def show_balance():
    print(f"your balance is : rs.{balance:.2f}")

def deposit():
    amount= float(input("enter an amount to be deposited:"))
    
    if amount<0:
        print("invalid amount")
        return 0
    else:
        return amount 
def withdraw():
    amount= float(input("enter an amount to be withdrawn: "))
    if amount >balance:
        print("insufficient balnce")
    elif amount<0 :
        print("invalid amount")
        return 0
    else:
        return amount 

balance=0 
is_running= True 

while is_running:
    print("banking program")
    print("1.show balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.exit")

    choice= input("enter your choice(1-4): ")


    if choice == "1":
        show_balance()
    elif choice == "2":
       balance += deposit()
    elif choice =="3":
       balance-= withdraw()
    elif choice =="4":
        is_running= False 
    else:
        print("invalid choice")

print("thank you")