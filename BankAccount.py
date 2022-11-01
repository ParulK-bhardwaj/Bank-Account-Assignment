# Import random module for random number generation
import random

class BankAccount:
    # routing number was not part of github requirement so did not add it here
    # https://github.com/Tech-at-DU/ACS-1111-Object-Oriented-Programming/blob/master/Lessons/bank_account.md
    # It can be easily added as <def __init__(self, full_name, routing_number = 123456789, account_type):> if needed
    def __init__(self, full_name, account_type):
        self.full_name = full_name.title()
        # generate 8 digit account number through random - added functionality based on rubric
        self.account_number = str(random.randint(10000000, 99999999))
        self.balance = 0
        self.account_type = account_type 

    # ---------------------------Deposit---------------------------
    # "%.2f" to get two digits after 2 decimals. round function was only giving one zero after decimal for the amount that were whole number. 
    def deposit(self, amount):
        self.balance = self.balance + amount
        self.balance_format = "%.2f" % float(self.balance)
        amount = "%.2f" % float(amount)
        print(f"Amount deposited: ${amount} New Balance: ${self.balance_format}")

     # ---------------------------Withdraw---------------------------   
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            overdraft_fee = 10
            self.balance = self.balance - overdraft_fee
            self.balance_format = "%.2f" % float(self.balance)
            overdraft_fee_format = "%.2f" % float(overdraft_fee)
            print(f"Overdraft fee: ${overdraft_fee_format} New Balance: ${self.balance_format}")
        else:
            self.balance = self.balance - amount
            self.balance_format = "%.2f" % float(self.balance)
            amount = "%.2f" % float(amount)
            print(f"Amount withdrawn: ${amount} New Balance: ${self.balance_format}")
    
    # ---------------------------Get Balance---------------------------  
    def get_balance(self):
        self.balance_format = "%.2f" % float(self.balance)
        print(f"Your Account Balance is ${self.balance_format}")
        return self.balance

    # ---------------------------Add interest--------------------------  
    def add_interest(self):
        if self.account_type.lower() == "checking":
            interest = float(self.balance) * 0.00083
            self.balance = float(self.balance) + interest
        elif self.account_type.lower() == "savings":
            interest = float(self.balance) * 0.001
            self.balance = float(self.balance) + interest
    
    # ---------------------------Add interest--------------------------  
    # Updated the name to titlel case using .title()
    # A string is a list in python so to call all the numbers from the last 4th element in the list. I called the -4 index to the last element in the string.
    def print_statement(self):
        truncated_account_number = "*" * (len(self.account_number)-4) + self.account_number[-4:]
        self.balance_format = "%.2f" % float(self.balance)
        print(f"{self.full_name}\nAccount No.: {truncated_account_number}\nAccount Type: {(self.account_type).title()}\nBalance: ${self.balance_format}")


parul_account = BankAccount("parul Bhardwaj", "savings")
ivan_account = BankAccount("ivan dubey", "savings")
noah_account = BankAccount("Noah dubey", "Checking")
mitchell_account = BankAccount("Mitchell hud", "savings")

bank = [parul_account, ivan_account, noah_account, mitchell_account]


# ---------------------------Bank list loop Add Interest--------------------------  
# Looping through bank list to add_interest to each account
# Decided to add account.print_statement to the method, can easily be removed and truned into new function if needed.
def bank_add_interest(bank):
    for account in bank:
        account.add_interest()
        account.print_statement()
        print("")

# ---------------------------Calling the functions--------------------------  
# add_interest Loop for Bank list
bank_add_interest(bank)
print()
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