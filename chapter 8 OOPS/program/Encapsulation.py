# Encapsulation Example in Python

class BankAccount():
    def __init__(self):
        # Private variable (encapsulation) - balance is hidden from outside
        self.__balance = 100000  

    def deposit(self, amount):
        # Method to add money to balance
        self.__balance += amount
        return self.__balance

    def withdrawn(self, amount):
        # Method to withdraw money with overdraft protection
        if amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            print("Insufficient funds!")  # Safety check

    def get(self):
        # Method to access private balance safely
        return self.__balance


# Object creation
s = BankAccount()

# Deposit money
s.deposit(int(input("Enter the amount to deposit: ")))

# Withdraw money
s.withdrawn(int(input("Enter the amount to withdraw: ")))

# Balance check
n = input("Do you want to check the balance? (yes/no): ")

if n.lower() == "yes":   # .lower() handles Yes/YES/yes
    print("Your balance is:", s.get())
elif n.lower() == "no":
    print("Thank you for your session...\nHave a GOOD day!")
else:
    print("Invalid answer")
