
# Simple Bank Account System
# A console-based banking application that supports multiple accounts,
# deposits, withdrawals, transfers, and transaction history.


import datetime
import random


# =============================================================================
# TRANSACTION CLASS
# Represents a single transaction (deposit, withdrawal, or transfer)
# =============================================================================

class Transaction:
    def __init__(self, txn_type, amount, description=""):
        """
        Initialize a transaction record.
        :param txn_type: Type of transaction - 'Deposit', 'Withdrawal', 'Transfer In', 'Transfer Out'
        :param amount: The monetary amount involved
        :param description: Optional note about the transaction
        """
        self.txn_type = txn_type
        self.amount = amount
        self.description = description
        # Automatically record the timestamp when the transaction is created
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        """Return a formatted string representation of this transaction."""
        sign = "+" if self.txn_type in ("Deposit", "Transfer In") else "-"
        return (f"[{self.timestamp}] {self.txn_type:<14} "
                f"{sign}₹{self.amount:>10.2f}   {self.description}")


# =============================================================================
# BANK ACCOUNT CLASS
# Core class representing an individual bank account
# =============================================================================

class BankAccount:
    def __init__(self, owner, initial_balance=0.0):
        """
        Create a new bank account.
        :param owner: Name of the account holder
        :param initial_balance: Starting balance (default is 0)
        """
        self.owner = owner
        self.balance = initial_balance
        # Generate a random 6-digit account number
        self.account_number = random.randint(100000, 999999)
        # List to store all Transaction objects for this account
        self.transactions = []

        # Record the opening deposit if an initial balance was provided
        if initial_balance > 0:
            self.transactions.append(
                Transaction("Deposit", initial_balance, "Account opening balance")
            )

    # -------------------------------------------------------------------------
    # DEPOSIT METHOD
    # -------------------------------------------------------------------------
    def deposit(self, amount, description="Deposit"):
        """
        Add funds to the account.
        :param amount: Amount to deposit (must be positive)
        :param description: Optional label for this deposit
        """
        if amount <= 0:
            print("  ❌ Deposit amount must be greater than zero.")
            return False

        self.balance += amount
        self.transactions.append(Transaction("Deposit", amount, description))
        print(f"  ✅ ₹{amount:.2f} deposited successfully. New balance: ₹{self.balance:.2f}")
        return True

    # -------------------------------------------------------------------------
    # WITHDRAWAL METHOD
    # -------------------------------------------------------------------------
    def withdraw(self, amount, description="Withdrawal"):
        """
        Remove funds from the account.
        :param amount: Amount to withdraw (must be positive and within balance)
        :param description: Optional label for this withdrawal
        """
        if amount <= 0:
            print("  ❌ Withdrawal amount must be greater than zero.")
            return False

        if amount > self.balance:
            print(f"  ❌ Insufficient funds. Available balance: ₹{self.balance:.2f}")
            return False

        self.balance -= amount
        self.transactions.append(Transaction("Withdrawal", amount, description))
        print(f"  ✅ ₹{amount:.2f} withdrawn successfully. New balance: ₹{self.balance:.2f}")
        return True

    
    # TRANSFER METHOD
    #
    def transfer(self, target_account, amount):
        """
        Transfer funds from this account to another account.
        :param target_account: The BankAccount object to receive funds
        :param amount: Amount to transfer
        """
        description_out = f"Transfer to {target_account.owner} (A/C {target_account.account_number})"
        description_in  = f"Transfer from {self.owner} (A/C {self.account_number})"

        # Withdraw from sender; only proceed if successful
        if self.withdraw(amount, description_out):
            # Manually log a 'Transfer Out' entry instead of a generic withdrawal
            self.transactions[-1] = Transaction("Transfer Out", amount, description_out)
            # Deposit into receiver
            target_account.balance += amount
            target_account.transactions.append(
                Transaction("Transfer In", amount, description_in)
            )
            print(f"  ✅ ₹{amount:.2f} transferred to {target_account.owner}.")

    # 
    # STATEMENT / HISTORY METHOD
    # 
    def print_statement(self):
        """Display a formatted mini bank statement for this account."""
        print(f"\n  {'=' * 65}")
        print(f"  Account Statement — {self.owner} | A/C No: {self.account_number}")
        print(f"  {'=' * 65}")

        if not self.transactions:
            print("  No transactions found.")
        else:
            for txn in self.transactions:
                print(f"  {txn}")

        print(f"  {'-' * 65}")
        print(f"  Current Balance: ₹{self.balance:.2f}")
        print(f"  {'=' * 65}\n")

    def __str__(self):
        """Short summary of the account."""
        return f"  {self.owner:<20} | A/C: {self.account_number} | Balance: ₹{self.balance:.2f}"


# BANK CLASS
# Manages a collection of accounts and provides the top-level menu


class Bank:
    def __init__(self, name):
        """
        Initialize the bank with a name and an empty account registry.
        :param name: Name of the bank
        """
        self.name = name
        # Dictionary mapping account_number -> BankAccount object
        self.accounts = {}

    def create_account(self, owner, initial_balance=0.0):
        """Create a new account and register it with the bank."""
        account = BankAccount(owner, initial_balance)
        self.accounts[account.account_number] = account
        print(f"\n  ✅ Account created for {owner}. Account No: {account.account_number}")
        return account

    def find_account(self, account_number):
        """
        Look up an account by its number.
        :return: BankAccount if found, else None
        """
        account = self.accounts.get(account_number)
        if not account:
            print("  ❌ Account not found. Please check the account number.")
        return account

    def list_accounts(self):
        """Print a summary of all accounts held in this bank."""
        print(f"\n  {'=' * 55}")
        print(f"  All Accounts — {self.name}")
        print(f"  {'=' * 55}")
        if not self.accounts:
            print("  No accounts found.")
        else:
            for acc in self.accounts.values():
                print(acc)
        print(f"  {'=' * 55}\n")


# =============================================================================
# MAIN MENU — Entry point for the application
# =============================================================================

def get_float(prompt):
    """Helper to safely read a positive float from the user."""
    try:
        value = float(input(prompt))
        return value
    except ValueError:
        print("  ❌ Invalid amount. Please enter a numeric value.")
        return None

