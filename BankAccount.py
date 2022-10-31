class BankAccount:
    def __init__(self, full_name, account_number, account_type):
        self.full_name = full_name.title()
        self.account_number = account_number
        self.balance = 0
        self.account_type = account_type  

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.balance_format = "%.2f" % float(self.balance)
        amount = "%.2f" % float(amount)
        print(f"Amount deposited: ${amount} New Balance: ${self.balance_format}.")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            overdraft_fee = 10
            self.balance = self.balance - overdraft_fee
            self.balance_format = "%.2f" % float(self.balance)
            overdraft_fee_format = "%.2f" % float(overdraft_fee)
            print(f"Overdraft fee: ${overdraft_fee_format} New Balance: ${self.balance_format} ")
        else:
            self.balance = self.balance - amount
            self.balance_format = "%.2f" % float(self.balance)
            amount = "%.2f" % float(amount)
            print(f"Amount withdrawn: ${amount} New Balance: ${self.balance_format}.")
    
    def get_balance(self):
        self.balance_format = "%.2f" % float(self.balance)
        print(f"Your Account Balance is ${self.balance_format}.")
        return self.balance

    def add_interest(self):
        if self.account_type.lower() == "checking":
            interest = float(self.balance) * 0.00083
            self.balance = float(self.balance) + interest
        elif self.account_type.lower() == "savings":
            interest = float(self.balance) * 0.001
            self.balance = float(self.balance) + interest
    
    # Updated the name to titlel case using .title()
    # A string is a list in python so to call all the numbers from the last 4th element in the list. I called the -4 index to the last element in the string.
    def print_statement(self):
        truncated_account_number = "*" * (len(self.account_number)-4) + self.account_number[-4:]
        self.balance_format = "%.2f" % float(self.balance)
        print(f"{self.full_name}\nAccount No.: {truncated_account_number}\nBalance: ${self.balance_format}")


parul_account = BankAccount('parul Bhardwaj', '45678912', "savings")
ivan_account = BankAccount('ivan dubey', '56712311', "savings")
danielle_account = BankAccount('Danielle Roxberry', '12369349', "Checking")
mitchell_account = BankAccount('Mitchell hudson', '03141592', "savings")

bank = [parul_account, ivan_account, danielle_account, mitchell_account]

parul_account.get_balance()
parul_account.add_interest()
parul_account.withdraw(4000.34)
parul_account.withdraw(400)
parul_account.deposit(300)
parul_account.print_statement()
print("\nMoney Deposited")
mitchell_account.deposit(400000)
mitchell_account.print_statement()
print("\nInterest Added")
mitchell_account.add_interest()
mitchell_account.print_statement()
print("\nMoney Withdrawn")
mitchell_account.withdraw(150)
mitchell_account.print_statement()
