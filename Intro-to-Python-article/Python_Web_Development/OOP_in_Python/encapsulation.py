class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder  # Private attribute
        self.__balance = balance                # Private attribute

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

# Creating an instance of BankAccount
account = BankAccount("John Doe", 1000)

# Accessing methods (encapsulation hides the implementation details)
account.deposit(500)
account.withdraw(200)
print("Current Balance:", account.get_balance())
