# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the account with an optional starting balance."""
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist. Returns True if successful."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
