import sys

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        if amount > self.__account_balance or amount < 0:
            return False
        self.__account_balance -= amount
        return True

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")


def main():
    account = BankAccount(100)  # Initial balance

    if len(sys.argv) < 2:
        print("Usage: python bank_account_main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_data = sys.argv[1]
    if ':' in command_data:
        command, amount_str = command_data.split(':', 1)
        try:
            amount = float(amount_str)
        except ValueError:
            print("Invalid amount. Please provide a numeric value.")
            sys.exit(1)
    else:
        command = command_data
        amount = None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command or missing amount.")

if __name__ == "__main__":
    main()
