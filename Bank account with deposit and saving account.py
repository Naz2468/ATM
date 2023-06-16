


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Added interest of {interest}. New balance: {self.balance}")


# Example usage
deposit_account = BankAccount("123456")
deposit_account.deposit(1000)
deposit_account.withdraw(500)
print(f"Deposit Account Balance: {deposit_account.get_balance()}")

savings_account = SavingsAccount("789012")
savings_account.deposit(2000)
savings_account.add_interest()
print(f"Savings Account Balance: {savings_account.get_balance()}")
