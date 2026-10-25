#Q8.Write a program to demonstrate encapsulation and abstraction using classes. 
from abc import ABC, abstractmethod

# Abstraction
class BankAccount(ABC):

    @abstractmethod
    def withdraw(self, amount):
        pass


# Encapsulation + Abstraction
class SavingsAccount(BankAccount):

    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.__balance)


account = SavingsAccount(5000)

account.withdraw(1000)
account.show_balance()
