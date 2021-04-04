import sys


class Customer:
    """simple bank database application"""

    bank_name = "Mutual Trust Limited"

    def __init__(self, customer_name, balance=0.0):
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Balance After Deposit: ", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("You don't have sufficient amount: ")
            sys.exit()

        self.balance = self.balance - amount
        print("Balance after withdraw: ", self.balance)


print("Welcome to ", Customer.bank_name)

customer_name = input("Enter your name: ")
c = Customer(customer_name)


while True:
    print("d - Deposit\nw - Withdraw\ne - Exit")

    option = input("Choose Your Option: ")

    if option == "d" or option == "D":
        amount = float(input("Enter Amount to deposit: "))
        c.deposit(amount)

    elif option == "w" or option == "W":
        amount = float(input("Enter amount to withdraw: "))
        c.withdraw(amount)

    elif option.lower() == "e":
        print("Thank you for Banking")
        sys.exit()
    else:
        print("Print chose correct option")

