from decimal import Decimal


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = round(Decimal(balance),2)
        print(f"Банковский счет на имя {self.name} создан. Текущий баланс: {self.__balance}")

    def withdraw_money(self, money):
        if self.__balance >= money:
            self.__balance = round(Decimal(self.__balance) - Decimal(money), 2)
            print(f"Произведено снятие. Текущий баланс: {self.__balance}")
        else:
            print(f"Недостаточно средств на счете. Текущий баланс: {self.__balance}")

    def put_money(self, money):
        self.__balance = round(Decimal(self.__balance) + Decimal(money), 2)
        print(f"Счет пополнен. Текущий баланс: {self.__balance}")


