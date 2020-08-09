#the class BankAccount needs to come first because python reads top down, and also BankAccount is called within the Class Users. It behaves like a function where you can call a function within a function
class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.interest_earned = 0
        if balance>0:
            self.balance = balance
        else:
            self.balance=0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance <= amount:
            self.balance -= 5
            print("Your balance is low, charging a $5 fee")
        else:
            self.balance -= amount
        return self

    def yield_interest(self):
        self.interest_earned += ((self.int_rate/100)*self.balance)
        # print(f"Your interest rate is {self.int_rate}, and your interest earned is {self.interest_earned}")
        return self

    def display_account_info(self):
        print(f"You have an interest rate of {self.int_rate}%, with an account balance of ${self.balance}. The amount of interest earned is ${self.interest_earned}")
        return self

class Users:
    def __init__(self, name, email, int_rate, balance):
        self.name=name
        self.email=email
        self.account = BankAccount(int_rate,balance)

    def make_deposit(self, amount):
        self.account.balance = self.account.balance + amount
        print("Deposited:",amount)
        return self

    def make_withdrawal(self, amount):
        self.account.balance = self.account.balance - amount
        print("Withdrawn:", amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}"'\n')
        return self

# Ricky = BankAccount(.3, 1000)
# Sukhpreet = BankAccount(.43, 2000)

Ricky = Users("Ricky Dhanota", "rickdhanota@gmail.com", .3, 1000)
Sukhpreet = Users("Sukhpreet Gill", "preetxgill@gmail.com", .43, 2000)


Ricky.make_deposit(800).make_deposit(350).make_deposit(270).make_withdrawal(400).display_user_balance()

Sukhpreet.make_deposit(1000).make_deposit(600).make_withdrawal(800).make_withdrawal(100).display_user_balance()

Sukhpreet.account.yield_interest().display_account_info()

Ricky.account.deposit(100).deposit(300).display_account_info() #This is doing the deposit method from within the class BankAccount



