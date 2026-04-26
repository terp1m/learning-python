from datetime import datetime

def save_balance(balance):
    with open("balance.txt", "w") as f:
                f.write(str(balance))

def log(action,amount,balance):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("history.txt", "a") as f:
        f.write(f"[{time}] {action} {amount},balance = {balance}\n")

try:
    with open("balance.txt", "r") as f:
        balance = int(f.read())
except FileNotFoundError:
    balance = 0

while True:
    print("1. Add money")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    choice = str(input("What are u picking:"))

    if choice == "1":
        amount = int(input("How much to add: "))
        balance += amount

        save_balance(balance)
        log("Added",amount,balance)

    elif choice == "2":
        amount = int(input("How much to withdraw:"))
        if amount > balance:
            print("Not enough money")
        else:
            balance -= amount
            save_balance(balance)
            log("Withdrew",amount,balance)

    elif choice == "3":
        print("Your balance is:", balance)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
