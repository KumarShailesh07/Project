class Account:
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self,amount):
        self.balance -= amount
        print(f'Rs.{amount} is debited')
        print(f'Your balance is {self.balance}')

    def credit(self,amount):
        self.balance += amount
        print(f'Rs.{amount} is credited')
        print(f'Your balance is {self.balance}')

    def get_balance(self):
        return self.balance

Acc1 = Account(10000,123456)
print('Balance:',Acc1.balance)
Acc1.debit(1000)
Acc1.credit(40000)
Acc1.debit(5500)