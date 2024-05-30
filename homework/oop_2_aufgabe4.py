class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, owner, interest_rate):
        super().__init__(account_number, balance, owner)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest. New balance is {self.balance}.")

# Erstelle ein Objekt savings1
savings1 = SavingsAccount(987654321, 2000, "Thomas Müller", 0.015)

# Zinsen anwenden
savings1.apply_interest()

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, owner, transaction_fee):
        super().__init__(account_number, balance, owner)
        self.transaction_fee = transaction_fee

    def deposit(self, amount):
        self.balance += amount - self.transaction_fee
        print(f"Deposited {amount} with a transaction fee of {self.transaction_fee}. New balance is {self.balance}.")

    def withdraw(self, amount):
        total_amount = amount + self.transaction_fee
        if total_amount <= self.balance:
            self.balance -= total_amount
            print(f"Withdrew {amount} with a transaction fee of {self.transaction_fee}. New balance is {self.balance}.")
        else:
            print(f"Insufficient funds. Current balance is {self.balance}.")

# Erstelle ein Objekt checking1
checking1 = CheckingAccount(1122334455, 1500, "Eva Becker", 2)

# Einzahlung
checking1.deposit(300)

# Abhebung
checking1.withdraw(100)
