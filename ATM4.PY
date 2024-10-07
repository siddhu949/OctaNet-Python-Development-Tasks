import json
import os

class ATM:
    def __init__(self):
        self.data_file = 'atm_data.json'
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                self.balance = data.get('balance', 0)
                self.pin = data.get('pin', "1234")
                self.transaction_history = data.get('transaction_history', [])
        else:
            self.balance = 1000  # Default initial balance
            self.pin = "1234"    # Default initial PIN
            self.transaction_history = []

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump({
                'balance': self.balance,
                'pin': self.pin,
                'transaction_history': self.transaction_history
            }, file)

    def authenticate(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your 4-digit PIN: ")
            if entered_pin == self.pin:
                print("PIN accepted.")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. You have {attempts} attempts left.")
        print("Too many incorrect attempts. Access denied.")
        return False

    def display_balance(self):
        print(f"Your account balance is: ${self.balance:.2f}")

    def withdraw_cash(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount:.2f}")
            self.save_data()
            print(f"Please take your cash: ${amount:.2f}")
        else:
            print("Insufficient funds.")

    def deposit_cash(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount:.2f}")
        self.save_data()
        print(f"Successfully deposited: ${amount:.2f}")

    def change_pin(self):
        new_pin = input("Enter new 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            self.pin = new_pin
            self.save_data()
            print("PIN successfully changed.")
        else:
            print("Invalid PIN. Please enter a 4-digit number.")

    def view_transaction_history(self):
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions to display.")

    def display_menu(self):
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. View Transaction History")
        print("6. Exit")

def main():
    atm = ATM()

    if atm.authenticate():
        while True:
            atm.display_menu()
            choice = input("Choose an option (1-6): ")

            if choice == '1':
                atm.display_balance()
            elif choice == '2':
                atm.withdraw_cash()
            elif choice == '3':
                atm.deposit_cash()
            elif choice == '4':
                atm.change_pin()
            elif choice == '5':
                atm.view_transaction_history()
            elif choice == '6':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

