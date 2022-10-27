class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Amount deposited: ${amount} New Balance: ${self.balance}.")
    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"Amount withdrawn: ${amount} New Balance: ${self.balance}.")

bank_account = BankAccount('parul Bhardwaj', '456789', 4000)
bank_account.deposit(300.14)