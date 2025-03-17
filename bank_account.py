class BankAccount:
    total_accounts = 0  
   
    def __init__(self, account_holder, initial_balance=0):
        """Initialize a new bank account."""
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []  # List to store transaction history
        BankAccount.total_accounts += 1  # Increment total account count

    def deposit(self, amount):
        """Instance method to deposit money into the account."""
        if self.validate_amount(amount):
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            return f"Deposit successful! New balance: ${self.balance}"
        return "Invalid deposit amount!"

    def withdraw(self, amount):
        """Instance method to withdraw money, applying a transaction fee."""
        transaction_fee = 2  # Fixed transaction fee
        total_withdrawal = amount + transaction_fee

        if self.validate_amount(amount) and self.balance >= total_withdrawal:
            self.balance -= total_withdrawal
            self.transaction_history.append(f"Withdrawn: ${amount} (Fee: ${transaction_fee})")
            return f"Withdrawal successful! New balance: ${self.balance}"
        return "Insufficient funds or invalid amount!"

    def transfer(self, recipient, amount):
        """Instance method to transfer money between two accounts."""
        if isinstance(recipient, BankAccount) and self.validate_amount(amount) and self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred: ${amount} to {recipient.account_holder}")
            recipient.transaction_history.append(f"Received: ${amount} from {self.account_holder}")
            return f"Transfer successful! New balance: ${self.balance}"
        return "Invalid transfer amount or insufficient funds!"

    def check_balance(self):
        """Instance method to check the current balance."""
        return f"Current balance: ${self.balance}"

    def get_transaction_history(self):
        """Instance method to return a list of all transactions."""
        return self.transaction_history if self.transaction_history else ["No transactions yet."]

    @classmethod
    def total_bank_accounts(cls):
        """Class method to return the total number of accounts."""
        return f"Total bank accounts: {cls.total_accounts}"

    @staticmethod
    def validate_amount(amount):
        """Static method to check if an amount is valid (positive, within limits)."""
        return isinstance(amount, (int, float)) and amount > 0

# Example Usage:
account1 = BankAccount("Alice", 500)
account2 = BankAccount("Bob", 300)

print(account1.deposit(200))
print(account1.withdraw(100))
print(account1.transfer(account2, 150))
print(account1.check_balance())
print(account2.check_balance())
print(account1.get_transaction_history())
print(account2.get_transaction_history())
print(BankAccount.total_bank_accounts())
