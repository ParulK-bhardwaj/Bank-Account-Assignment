from pytest import console_main


class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Amount deposited: ${float(amount)} New Balance: ${float(self.balance)}.")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            overdraft_fee = 10
            self.balance = self.balance - overdraft_fee
            print(f"Overdraft fee: ${overdraft_fee} New Balance: ${float(self.balance)} ")
        else:
            self.balance = self.balance - amount
            print(f"Amount withdrawn: ${float(amount)} New Balance: ${float(self.balance)}.")
    
    def get_balance(self):
        print(f"Your Account Balance is {self.balance}.")
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance = self.balance + interest
    
    # -------------TODO float 2 decimal places---------------- 
    # -------------TODO update the name to pascal case---------------- 
    # A string is a list in python so to call all the numbers from the last 4th element in the list. I called the -4 index to the last element in the string.
    def print_statement(self):
        truncated_account_number = "*" * (len(self.account_number)-4) + self.account_number[-4:]
        print(f"{self.full_name}\nAccount No.: {truncated_account_number}\nBalance: ${float(self.balance)}")


parul_account = BankAccount('Parul Bhardwaj', '45678912', 4000)
mitchell_account = BankAccount('Mitchell Hudson', '56712311', 10000)
danielle_account = BankAccount('Danielle Roxberry', '12369349', 12000)
parul_account.print_statement()