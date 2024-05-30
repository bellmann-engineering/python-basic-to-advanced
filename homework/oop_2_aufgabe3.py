class BankAccount:
    def __init__(self, account_number, balance, owner):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print(f"Insufficient funds. Current balance is {self.balance}.")

# Erstelle ein Objekt account1
account1 = BankAccount(123456789, 1000, "Lisa Schmidt")

# Einzahlung
account1.deposit(500)

# Abhebung
account1.withdraw(200)

# Abhebung mit unzureichendem Guthaben
account1.withdraw(1500)
