from abc import ABC , abstractclassmethod

class Customer():
    
    def __init__(self,name,lastName,address,id,password):
        self.name = name
        self.lastName = lastName
        self.address = address
        self.id = id
        self.password = password


class BankAccount():
    def __init__(self,balance,credit,accountID):
        pass

    def moneyTransfer():
        pass
    
    def moneyDeposit():
        pass

    def moneyWithdraw():
        pass

    def takeCredit():
        pass