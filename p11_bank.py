class Account:
    def __init__(self,name,balance,min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds!")

    def statement(self):
        print("Account Balance: Rs. {}".format(self.balance))

class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)

    def __str__(self):
        return "{}'s Current Account : Balance Rs. {}".format(self.name, self.balance)

class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)

    def __str__(self):
        return "{}'s Savings Account : Balance Rs. {}".format(self.name, self.balance)

s = Current("Senjuti", 100000)
print(s)
s.deposit(400)
print(s)
s.withdraw(100)
s.statement()
#s.withdraw(1000000)
t = Current("Tanmoy", 1000000)
print(t)
t.deposit(400)
print(t)
t.withdraw(100)
t.statement()
