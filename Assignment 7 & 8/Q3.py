class Customer:
    def __init__(self, name, account_number, balance=0.0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.account_number}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")
        return self.balance

class Bank:
    def __init__(self):
        self.customers = {}

    def add_customer(self, name, account_number, initial_balance=0.0):
        if account_number not in self.customers:
            self.customers[account_number] = Customer(name, account_number, initial_balance)
            print(f"Customer {name} added with account number {account_number}.")
        else:
            print("Account number already exists.")

    def get_customer(self, account_number):
        return self.customers.get(account_number, None)

# Example usage:
if __name__ == "__main__":
    bank = Bank()
    bank.add_customer("Alice", 1001, 500.0)
    bank.add_customer("Bob", 1002, 1000.0)
    
    alice = bank.get_customer(1001)
    if alice:
        alice.deposit(200)
        alice.withdraw(100)
        alice.get_balance()
    
    bob = bank.get_customer(1002)
    if bob:
        bob.withdraw(500)
        bob.get_balance()