import random 

def spin_row():
     symbols = ["✨", "🎂", "🌹", "🎁", "💕"]

     return [random.choice(symbols) for _ in range(3)]
def print_row(row):
     print (" | ", " | ".join(row), "|")
def get_payout(row, bet):
     if row[0] == row[1] == row[2]:
         if row[0] == "✨":
             return bet* 3 
         elif row[0] == "🎂":
             return bet* 5
         elif row[0] == "🌹":
             return bet* 10
         elif row[0] == "🎁":
             return bet* 15
         elif row[0] == "💕":
             return bet* 20
              
def main():
    balance = 100


    print("*********************")
    print("welcome to python slot")
    print("symbols: ✨ 🎂 🌹 🎁 💕")
    print("*********************")

    while balance > 0:
        print(f"your balance is : rs.{balance}")

        bet = input("enter your bet amount: ")

        if not bet.isdigit():
            print("please enter valid number")
            continue 
        bet = int(bet)

        if bet > balance:
            print("insufficient funds")
            continue

        if bet<=0:
            print("bet must be greater than 0")
            continue
        
        balance-= bet

        row= spin_row()
        print("spinnng,....\n")
        print_row(row)

        payout = get_payout(row, bet)


if __name__ == "__main__":
    main()