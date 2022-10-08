""" 
Change the CheckingAccount class in How To 10.1 so that a $1 fee is levied for deposits or withdrawals in excess of three free monthly transactions. 
Place the code for computing the fee into a separate method that you call from the deposit and withdraw methods.
"""
## This module defines a BankAccount class
#

## A bank account has a balance and a mechanism for applying interest or fees at # the end of the month.
#
class BankAccount :
    ## Constructs a bank account with zero balance. 
    # 
    def __init__(self) :
        self._balance = 0.0
    
    ## Makes a deposit into this account.
    # @param amount the amount of the deposit 
    #
    def deposit(self, amount) :
        self._balance = self._balance + amount
    
    ## Makes a withdrawal from this account, or charges a penalty if
    # sufficient funds are not available.
    # @param amount the amount of the withdrawal 
    # 
    def withdraw(self, amount) : 
        self._balance = self._balance - amount
    
    ## Carries out the end of month processing that is appropriate
    # for this account.
    #
    def monthEnd(self) :
        raise NotImplementedError
    
    ## Gets the current balance of this bank account. # @return the current balance
    #
    def getBalance(self) :
        return self._balance


## A savings account earns interest on the minimum balance. 
# 
class SavingsAccount(BankAccount) :
    ## Constructs a savings account with a zero balance. 
    # 
    def __init__(self) :
        super().__init__()
        self._interestRate = 0.0
        self._minBalance   = 0.0

    ## Sets the interest rate for this account.
    # @param rate the monthly interest rate in percent 
    # 
    def setInterestRate(self, rate) :
        self._interestRate = rate
    
    # These methods override superclass methods. 
    def withdraw(self, amount) :
        super().withdraw(amount)
        balance = self.getBalance()
        if balance < self._minBalance :
            self._minBalance = balance
    
    def monthEnd(self) : 
        interest = self._minBalance * self._interestRate / 100 
        self.deposit(interest)
        self._minBalance = self.getBalance()


## A checking account has a limited number of free deposits and withdrawals
#
class CheckingAccount(BankAccount) :
    ## Constructs a checking account with a zero balance (instance var from superclass)
    ## To address the task we need to keep count of transactions per period
    ## The instance variable _transactions will keep of track of number of transactions
    # 
    def __init__(self) :
        super().__init__()
        self._transactions = 0
        self._fee          = 0

    ## Introducing additional method that returns curent fee charged
    #  
    def getFee(self) :
        if self._transactions > 3 :
            self._fee = 1
        else:
            self._fee = 0
        return self._fee

    ## Each time the function will be called amount performed transactions will increase by 1
    ## then the function will check whether number of transaction during the month exceeds 3
    ## and return 1 if it does and 0 
    #
    def feePmt(self) :
        self._transactions = self._transactions + 1
        if self._transactions > 3 :
            self._fee = 1
        else:
            self._fee = 0
        return self.getFee()
            
    ## Override the deposit method: deposit puts the money on account, however, we have to subtract the fee
    #
    def deposit(self, amount):
        super().deposit(amount - self.feePmt())

    ## Override the withdraw method: since the witdraw method sutracts the amount the account, we need to increase amount by fee
    #
    def withdraw(self, amount) :
        super().withdraw(amount + self.feePmt())

    ## Override the monthEnd method: set the number of transactions back to zero
    #
    def monthEnd(self) : 
        self._transactions = 0
