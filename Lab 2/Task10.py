# Task#10:
# Secure Banking System (Encapsulation):
# Create a BankAccount class with:
# • Private attribute __balance
# • Public methods: deposit(), withdraw(), get_balance()
# Demonstrate that __balance cannot be accessed directly from outside the class.

class BankAccount:
    def __init__(self, account_holder, account_no, balance):
        self.account_holder = account_holder
        self.account_no = account_no
        self.__balance = balance   

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")

    def get_balance(self):
        return self.__balance
        
acc1 = BankAccount("Abdul Majid", 101, 5000)
acc1.deposit(2000)
acc1.withdraw(1000)
print("Balance:", acc1.get_balance())
