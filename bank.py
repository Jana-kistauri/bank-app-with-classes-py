from datetime import datetime
import pytz

class Account:
    
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.history = []
    

    @staticmethod
    def _get_local_time():
        return pytz.utc.localize(datetime.utcnow()).astimezone().isoformat()


    def deposit(self, amount):
        self.balance += amount
        print(f"თქვენს ანაგარიშზე დაემატა {amount} ლარი")
        print(f"ბალანსი: {self.balance} ")
        self.history.append([self._get_local_time(), "+" + str(amount), self.balance])


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"თქვენს ანაგარიშიდან ჩამოიჭრა {amount} ლარი.")
            print(f"ბალანსი: {self.balance} ")
            self.history.append([self._get_local_time(), amount, self.balance])


    def show_balance(self):
        print(f"თქვენს ანაგარიშზე არის: {self.balance} ლარი")


    def show_history(self):
        for date, amount, balance in self.history:
            print(f"Date: {date}  Ammount: {amount}  balance: {balance}")