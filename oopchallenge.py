class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account Owner:   {self.owner}   Account Balance:    {self.balance}'

    def deposit(self, amount):
        self.balance += amount
        print('Deposit accepted')
        print(f'Balance now is: {self.balance}')

    def withdraw(self, amount):
        if (self.balance-amount < 0):
            print('Funds Unavailable')
            print(f'Balance is: {self.balance}')

        else:
            self.balance -= amount
            print('Withdrawal Accepted')
            print(f'Balance now is: {self.balance}')


acct1 = Account('Jose', 100)
# print(acct1)

acct1.withdraw(20)
