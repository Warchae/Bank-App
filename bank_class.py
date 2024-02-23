from abc import ABC , abstractclassmethod
from random import randint
import uuid

class Customer():
    
    def __init__(self,name,lastName,address,id,password):
        self.name = name
        self.lastName = lastName
        self.address = address
        self.id = id
        self.password = password

class BankAccount(Customer):
    
    def __init__(self, balance, accountID):
        self.balance = 0
        self.credit = 0
        self.accountID = str(uuid.uuid4().fields[-1])[:10]

    def __setMoney(self, ID, amount):
        if ID in "account.sql":
            BankAccount(self, balance, None, ID)
            balance = balance + amount
            print("Your Money Has Been Transfered To {} Account ID {} $ Successfully.".format(ID, amount))

    def getMoney(self):
        print("Your Balance: ", self.balance)
        return self.balance
        
    def moneyTransfer(self, amount, toID):    
        
        if self.balance < amount:
            print("Your Balance is Not Enough For Transfer!")
            return None
        
        elif self.ID == toID:
            print("You Can Not Transfer To Yourself!")
            return None
        
        elif toID not in "account.sql":
            print("Account ID not Valid.")
            return None
        
        else:
            self.balance = self.balance - amount
            self.__setMoney(toID,amount)

    def moneyDeposit(self, amount):
        self.balance = self.balance + amount
        print("New Balance: ",self.balance)
        return self.balance

    def moneyWithdraw(self, amount):
        self.balance = self.balance - amount
        print("New Balance: ", self.balance)
        return self.balance