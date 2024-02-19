import sys
import random
import logging

logging.basicConfig(level=logging.INFO)  

class Transaction:
    def __init__(self, type, amount, recipient=None):
        self.type = type
        self.amount = amount
        self.recipient = recipient

class ATM:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def account_detail(self):
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Available Balance: {self.balance}")

    def check_balance(self):
        print(f"Available Balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction("deposit", amount))
        print(f"Amount Deposited: {amount}")
        print(f"New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient balance")
        else:
            self.balance -= amount
            self.transactions.append(Transaction("withdraw", amount))
            print(f"Amount Withdrawn: {amount}")
            print(f"New Balance: {self.balance}")

    def transfer(self, amount, recipient_account):
        if amount > self.balance:
            print("Error: Insufficient balance")
        else:
            self.balance -= amount
            recipient_account.balance += amount
            self.transactions.append(Transaction("transfer", amount, recipient_account))
            recipient_account.transactions.append(Transaction("receive transfer", amount, self))
            print(f"Amount Transferred: {amount}")
            print(f"New Sender Balance: {self.balance}")
            print(f"New Recipient Balance: {recipient_account.balance}")

    def print_transaction_history(self):
        for i, transaction in enumerate(self.transactions, 1):
            if transaction.type == "deposit":
                print(f"{i}. Deposited {transaction.amount}")
            elif transaction.type == "withdraw":
                print(f"{i}. Withdrew {transaction.amount}")
            elif transaction.type == "transfer":
                print(f"{i}. Transferred {transaction.amount} to {transaction.recipient.account_number}")
            elif transaction.type == "receive transfer":
                print(f"{i}. Received transfer of {transaction.amount} from {transaction.recipient.account_number}")

    def transaction(self):
        while True:
            print("\nTransaction Menu")
            print("1. Account Detail")
            print("2. Check Balance")
            print("3. Transaction History")
            print("4. Withdraw")
            print("5. Deposit")
            print("6. Transfer")
            print("7. Exit")
            choice = input("Enter your choice: ")
            try:
                choice = int(choice)
            except ValueError:
                print("Invalid choice. Please enter a number.")
                continue
            if choice == 1:
                self.account_detail()
            elif choice == 2:
                self.check_balance()
            elif choice == 3:
                self.print_transaction_history()
            elif choice == 4:
                amount = input("Enter amount to withdraw: ")
                try:
                    amount = float(amount)
                    self.withdraw(amount)
                except ValueError:
                    print("Invalid amount. Please enter a number.")
            elif choice == 5:
                amount = input("Enter amount to deposit: ")
                try:
                    amount = float(amount)
                    self.deposit(amount)
                except ValueError:
                    print("Invalid amount. Please enter a number.")
            elif choice == 6:
                amount = input("Enter amount to transfer: ")
                recipient_account_number = input("Enter recipient account number: ")
                try:
                    amount = float(amount)
                    recipient_account_number = int(recipient_account_number)
                    recipient_account = None
                    for account in accounts:
                        if account.account_number == recipient_account_number:
                            recipient_account = account
                            break
                    if recipient_account:
                        self.transfer(amount, recipient_account)
                    else:
                        print("Recipient account not found.")
                except ValueError:
                    print("Invalid amount or recipient account number. Please enter valid numbers.")

            elif choice == 7:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

accounts = [
    ATM("Jay Thorat", 123456, 1000),
    ATM("Intern 1", 654321, 500),
]

while True:
    print("\nWelcome to ATM")
    print("Select Account:")
    for i, account in enumerate(accounts, 1):
        print(f"{i}. {account.name} ({account.account_number})")
    print(f"{len(accounts) + 1}. Exit")
    account_choice = input("Enter your choice: ")
    try:
        account_choice = int(account_choice)
        if 1 <= account_choice <= len(accounts):
            selected_account = accounts[account_choice - 1]
            selected_account.transaction()
        elif account_choice == len(accounts) + 1:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid account.")
    except ValueError:
        print("Invalid choice. Please enter a number.")
