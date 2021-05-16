import math
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

name = str(input("Input your Name: "))
balance = "x"
while balance.isdigit() == False:
    balance = input("Input your Balance: ")
    if balance.isdigit() == False:
        print("\nPlease enter a number!")
balance = int(balance)
acc = Account(name,balance)

while True: 
    print("\nMenu:\n1. Deposit\n2. Withdraw\n")

    menu = ["x"]
    while menu not in ["1","2"]:
        menu = input("Choose menu (1/2): ")
        if menu not in ["1","2"]:
            print("\nPlease enter the correct options!")


    if menu == "1":
        deposit = int(input("How much you need to deposit: "))
        print()
        print(acc.deposit(deposit))
        choose = ["x"]
        while choose not in ["Y","N"]:    
            choose = str(input("Another Transaction? (Y/N): ")).upper()
        if choose == "Y":
            pass
        if choose == "N":
            print("Thanks for the transaction")
            break

    elif menu == "2":
        withdraw = int(input("How much you need to withdraw: "))
        print()
        print(acc.withdraw(withdraw))        
        choose = ["x"]
        while choose not in ["Y","N"]:    
            choose = str(input("Another Transaction? (Y/N): ")).upper()
        if choose == "Y":
            pass
        if choose == "N":
            print("\nThanks for the transaction")
            break

    



    






    


