class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    # Getter method
    def get_balance(self):
        return self.__balance

    # Setter method
    def deposit(self, amount):
        self.__balance += amount
        print("Amount Deposited:", amount)


# Create object
account = BankAccount(1000)

# Access through methods
print("Balance:", account.get_balance())

account.deposit(500)

print("Updated Balance:", account.get_balance())