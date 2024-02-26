from abc import ABC
import uuid
import datetime


accounts = {}
customers = {}
int_rate = 3
low_int = int_rate * 1.5
med_int = int_rate * 1.8
high_int = int_rate
higher_int = int_rate * 0.8

class Customer():
    
    def __init__(self, name, lastName, address, id, password):
        self.name = name
        self.lastName = lastName
        self.address = address
        self.id = id
        self.password = password
        

class BankAccount(Customer):
    
    def __init__(self, accountID):
        self.accountID = accountID
        self.balance = 0  # Initialize balance
        self.loan = 0
        loanopen_datetime = 0

    def getMoney(self):
        print("Your Balance: ", self.balance)
        return self.balance

    def moneyDeposit(self, amount):
        self.balance += amount
        print("New Balance: ", self.balance)

    def moneyWithdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print("New Balance: ", self.balance)

    def takeCredit(self):
        print(
    f"""
        Credits Yearly Interest Range:
        0$ - 2500$ = {low_int}%
        2501$ - 5000$ = {med_int}%
        5000$ - 10000$ = {high_int}%
        +10000$ = {higher_int}%
    """)
        amount = int(input("How much loan would you like to take?: "))
        if amount <= 0:
            print("Amount must be positive!")
        elif self.loan > 1:
            print("You already have a loan!")
        elif self.balance < 0:
            print("You Can Not Take Loan While You Have Debt")
        else:
            now_datetime = datetime.datetime.now()
            strdate = now_datetime.strftime("%Y%m%d%H%M%S")
            self.loanopen_datetime = int(strdate)

            if amount > 0 and amount <=2500:
                self.balance += amount
                self.loan = amount
                print(f"You succesfully take loan {amount} at {self.loanopen_datetime}.")
            elif amount >= 2501 and amount <= 5000:
                self.balance += amount
                self.loan = amount
                print(f"You succesfully take loan {amount} at {self.loanopen_datetime}.")
            elif amount >= 5001 and amount <= 10000:
                self.balance += amount
                self.loan = amount
                print(f"You succesfully take loan {amount} at {self.loanopen_datetime}.")
            elif amount >= 10001:
                self.balance += amount
                self.loan = amount
                print(f"You succesfully take loan {amount} at {self.loanopen_datetime}.")
            else:
                print("You Can't Take Loan Succesfully.")

    def returnCredit(self):
        if self.loan <= 0:
            print("You Don't Have Any Credit")
        else:
            if self.loan > 0 and self.loan <= 2500:
                interest_rate = low_int
            elif self.loan > 2500 and self.loan <= 5000:
                interest_rate = med_int
            elif self.loan > 5000 and self.loan <= 10000:
                interest_rate = high_int
            else:
                interest_rate = higher_int

            time = datetime.datetime.now()
            stdate = time.strftime("%Y%m%d%H%M%S")
            current_time = int(stdate)
            bill = (interest_rate * (current_time - self.loanopen_datetime)) / (360*24*60*60) + self.loan
            print(self.loan, "of Loan Cost You With Interest", bill)
            self.balance = self.balance - bill
            self.loan = 0

    def moneyTransfer(self, amount, yourID, toID):    
        if accounts[yourID].balance < amount:
            print("Your Balance is Not Enough For Transfer!")
        elif yourID == toID:
            print("You Cannot Transfer To Yourself!")
        elif toID not in accounts:
            print("Account ID not Valid.")
        else:
            accounts[self.toID].balance += amount
            accounts[yourID].balance -= amount
            print("Your Transaction Was Succesfully Made!")
        
class exchangeRate():

    def __init__(self):
        self.__usdeuro = 0.98
        self.__usdau = 75
        self.__usdgp = 0.80
        
    def showExcRate(self):
        print("""
*****Exchange Rates*****
    USD / EURO = {}
    USD / GOLD = {}
    USD / STERLIN = {}
""".format(self.__usdeuro,self.__usdau,self.__usdgp))