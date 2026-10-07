class BankAccount:
    def __init__(self, balance = 1):
        self.__balance = balance 

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdrawn(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, balance=None, interest_rate=0.05):
        if balance is None:
            super().__init__()
        else:
            super().__init__(balance)
        self.__interest_rate = interest_rate

    def calculate_interest(self):
        return self.get_balance() * self.__interest_rate

    def add_interest(self):
        interest = self.calculate_interest()
        self.deposit(interest)
class CurrentAccount(BankAccount):
    def __init__(self, balance=None, overdraft_limit=5000):
        if balance is None:
            super().__init__()
        else:
            super().__init__(balance)
        self.__overdraft_limit = overdraft_limit

    def withdrawn(self, amount):
        if amount <= self.get_balance() + self.__overdraft_limit:
            self.deposit(-amount)  # Withdraw by depositing a negative amount   
            return self.get_balance()
        else:
            print("Overdraft limit exceeded!")


# -------- Interactive Usage --------
# Bank Account
balance = float(input("Enter initial Bank Account balance: "))
b = BankAccount(balance)
print("Bank Account Balance:", b.get_balance())

# Savings Account
print("\n------- Savings Account Example ---")
s_balance = input("Enter initial Savings Account balance OR press Enter to use Bank Account balance: ")
s = SavingsAccount(balance=b.get_balance() if s_balance.strip() == "" else float(s_balance), interest_rate=0.05)
deposit_amt = float(input("Enter amount to deposit in Savings Account: "))
s.deposit(deposit_amt)
print("After deposit, balance:", s.get_balance())
print("Before adding interest:", s.get_balance())

interest = s.calculate_interest()
print("Interest earned:", interest)

s.add_interest()
print("Final balance:", s.get_balance())

# Current Account
print("\n------- Current Account Example ---")
c_balance = input("Enter initial Current Account balance: ")
c = CurrentAccount(balance= float(c_balance) if c_balance.strip() else b.get_balance(), overdraft_limit=2000)
# c_balance.strip run if have content in it not if it uses the b.get_balance
print("Before account balance:", c.get_balance())

withdraw_amt1 = float(input("Enter amount to withdraw from Current Account: "))
c.withdrawn(withdraw_amt1)
print("Balance after withdrawal:", c.get_balance())

withdraw_amt2 = float(input("Enter another amount to withdraw from Current Account: "))
c.withdrawn(withdraw_amt2)
print("Balance after withdrawal:", c.get_balance())
