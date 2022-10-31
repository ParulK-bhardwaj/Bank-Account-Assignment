class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name.title()
        self.account_number = account_number
        self.balance = balance
        self.balance_format = "%.2f" % float(self.balance)
        

    def deposit(self, amount):
        self.balance = self.balance + amount
        amount = "%.2f" % float(amount)
        print(f"Amount deposited: ${amount} New Balance: ${self.balance_format}.")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            overdraft_fee = 10
            self.balance = self.balance - overdraft_fee
            overdraft_fee_format = "%.2f" % float(overdraft_fee)
            print(f"Overdraft fee: ${overdraft_fee_format} New Balance: ${self.balance_format} ")
        else:
            self.balance = self.balance - amount
            amount = "%.2f" % float(amount)
            print(f"Amount withdrawn: ${amount} New Balance: ${self.balance_format}.")
    
    def get_balance(self):
        print(f"Your Account Balance is ${self.balance_format}.")
        return self.balance

    def add_interest(self):
        interest = float(self.balance) * 0.00083
        self.balance = float(self.balance)+ interest
    
    # -------------TODO float 2 decimal places---------------- 
    # Updated the name to titlel case using .title()
    # A string is a list in python so to call all the numbers from the last 4th element in the list. I called the -4 index to the last element in the string.
    def print_statement(self):
        truncated_account_number = "*" * (len(self.account_number)-4) + self.account_number[-4:]
        print(f"{self.full_name}\nAccount No.: {truncated_account_number}\nBalance: ${self.balance_format}")


parul_account = BankAccount('parul Bhardwaj', '45678912', 4000)
mitchell_account = BankAccount('Mitchell Hudson', '56712311', 10000)
danielle_account = BankAccount('Danielle Roxberry', '12369349', 12000)
# parul_account.get_balance()
# parul_account.add_interest()
parul_account.withdraw(4000.34)
parul_account.deposit(300)
parul_account.print_statement()