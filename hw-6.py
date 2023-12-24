class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 1.0

    def withdraw_money(self, money):
        self.balance = self.balance - money

    def put_money(self, money):
        self.balance = self.balance + money
