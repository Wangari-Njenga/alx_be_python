from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Starting balance

    while True:
        print("\nChoose an operation: deposit, withdraw, display, or exit")
        command = input("Enter command: ").strip().lower()

        if command == "deposit":
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
                print(f"Deposited: ${amount:.2f}")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif command == "withdraw":
            try:
                amount = float(input("Enter amount to withdraw: "))
                if account.withdraw(amount):
                    print(f"Withdrew: ${amount:.2f}")
                else:
                    print("Insufficient funds.")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif command == "display":
            account.display_balance()
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()
