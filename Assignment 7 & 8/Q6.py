class BankAccount:
    def __init__(self, account_number, balance=0.0):
        """Initialize the bank account with an account number and an optional balance."""
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a specified amount from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            print("Withdrawal amount must be positive.")

    def display(self):
        """Display the account details."""
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ₹{self.balance}")

# Example Usage
account = BankAccount("123456789", 5000)
account.display()
account.deposit(2000)
account.withdraw(1000)
account.withdraw(7000)
account.display()
