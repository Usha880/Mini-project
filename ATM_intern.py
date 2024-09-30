class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdraw ${amount}")
        else:
            print("Insufficient funds!")

    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.name}")
        else:
            print("Insufficient funds!")

    def show_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

class ATM:
    def __init__(self):
        self.accounts = {"user1": ("Alice", 1000, "1234"), "user2": ("Bob", 500, "5678")}
        self.current_account = None

    def login(self):
        while True:
            user_id = input("Enter your ID: ")
            pin = input("Enter your PIN: ")

            if user_id in self.accounts and pin == self.accounts[user_id][2]:   # Changed PIN verification
                name, balance, _ = self.accounts[user_id]
                self.current_account = Account(name, balance)
                print(f"Welcome, {self.current_account.name}!")
                break
            else:
                print("Invalid ID or PIN. Please try again.")

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.current_account.deposit(amount)
        print(f"Deposited ${amount} successfully.")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if self.current_account.balance >= amount:  # Use current_account's balance
            self.current_account.balance -= amount
            self.current_account.transaction_history.append(f"Withdraw ${amount}")
            print(f"Withdraw ${amount} successfully.")
        else:
            print("Insufficient funds!")

    def transfer(self):
        amount = float(input("Enter amount to transfer: "))
        recipient_id = input("Enter recipient's ID: ")
        if recipient_id in self.accounts:
            recipient_name = self.accounts[recipient_id][0]
            recipient = Account(recipient_name)
            self.current_account.transfer(amount, recipient)
            print(f"Transferred ${amount} to {recipient.name} successfully.")
        else:
            print("Recipient's ID not found.")

    def show_transaction_history(self):
        self.current_account.show_transaction_history()

def main():
    atm = ATM()

    # Login
    atm.login()

    while True:
        print("\nSelect an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Show Transaction History")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm.deposit()
        elif choice == "2":
            atm.withdraw()
        elif choice == "3":
            atm.transfer()
        elif choice == "4":
            atm.show_transaction_history()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()