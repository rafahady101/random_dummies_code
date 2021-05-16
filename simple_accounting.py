class Account:

    def __init__(self,owner,balance=0):

        self.owner = owner
        self.balance = balance

    def __str__(self):

        return f"Account Owner: {self.owner}\nAccount Balance: {self.balance}"

    def deposit(self,dep_value):

        self.balance += dep_value
        return f"Added {dep_value} to the balance\nYour curent balance: {self.balance}"

    def withdraw(self,draw_value):

        if self.balance >= draw_value:
            self.balance -= draw_value
            return f"{draw_value} Withdrawal Accepted\nYour current Balance: {self.balance}"

        if self.balance < draw_value:
            return f"Funds Unavailable!"

acct1 = Account("Jose", 100)
print(acct1)
print("="*20)
print(acct1.owner)
print("="*20)
print(acct1.balance)
print("="*20)
print(acct1.deposit(50))
print("="*20)
print(acct1.withdraw(75))
print("="*20)
print(acct1.withdraw(500))



    






    


