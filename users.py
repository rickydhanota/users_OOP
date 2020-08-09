class Users:
    def __init__(self,name, email):
        self.name = name
        self.email = email
        self.account_balance=0

    def make_withdrawl(self, amount):
        if self.account_balance<amount:
            self.account_balance -= 5
            print('Insufficient funds: Charging a $5 fee')
        else:
            self.account_balance -= amount
            return self
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def display_user_balance(self):
        print(f'User:{self.name}, Account Balance = {self.account_balance}')
        return self
    
    def transfer_money(self, other_user, amount):
        other_user.account_balance -= amount
        self.account_balance += amount
        print(f'User: {self.name}, Account Balance: {self.account_balance}')
        print(f'{other_user.name} is transfering {amount} dollars to {self.name}. {other_user.name}s balance is now {other_user.account_balance}')
        return self

class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print('Insufficient funds: Charging a $5 fee')
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f'Account Balance = {self.balance}')
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
        return self

Ricky=Users("Ricky Dhanota", "rickdhanota@gmail.com")
Sukhpreet=Users("Sukhpreet Gill", "preetxgill@gmail.com")
Cleo = Users("Cleo Gill", "meowxgill@gmail.com")

# Ricky.make_deposit(200).make_deposit(100).make_deposit(300).make_withdrawl(50).display_user_balance()
# Sukhpreet.make_deposit(200).make_deposit(200).make_deposit(370).make_withdrawl(120).display_user_balance()

# Cleo.transfer_money(Sukhpreet, 100)
# Sukhpreet.display_user_balance()

ba1 = BankAccount(balance=100)
ba2 = BankAccount(.01, 500)

ba1.deposit(100).deposit(50).deposit(50).withdraw(100).yield_interest().display_account_info()
ba2.deposit(100).deposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()

