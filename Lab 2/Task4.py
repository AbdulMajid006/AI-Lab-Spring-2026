# Task#4:
# Bank Account Manager (Methods & Attributes):
# Create a BankAccount class with:
# • Attributes: account_holder, account_no, balance
# • Methods: deposit(amount), withdraw(amount), display_account()
# Create multiple accounts and perform transactions.

class BankAccount:
    def __init__(self, account_holder, account_no, balance):
        self.account_holder = account_holder
        self.account_no = account_no
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def display_account(self):
        print("Account Holder: ", self.account_holder)
        print("Account No: ", self.account_no)
        print("Balance: ", self.balance)
ba1 = BankAccount("Hassan", 12345, 1200)
ba2 = BankAccount("Aslam", 59122, 2500)
ba1.display_account()
ba2.display_account()
print("After Transactions")
ba1.deposit(1000)
ba2.withdraw(500)
ba1.display_account()
ba2.display_account()
