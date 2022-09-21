"""
Implement a class Portfolio. This class has two objects, checking and savings, of the type BankAccount that was developed in Worked Example 9.1 
(ch09/worked_example_1/ bankaccount.py in your code files). Implement four methods:
• def deposit(self, amount, account) 
• def withdraw(self, amount, account) 
• def transfer(self, amount, account) 
• def getBalance(self, account)
Here the account string is "S" or "C". For the deposit or withdrawal, it indicates which account is affected. 
For a transfer, it indicates the account from which the money is taken; the money is automatically transferred to the other account.
"""
import os
path = "/Users/jakovsem/Documents/skole/MSc in Quantitative Finance/3rd semester/GRA 4152 - Object Oriented Programming/HW/Lecture 4"
os.chdir(path)
from W9_1 import BankAccount

class Portfolio:
  # initialize two types of account. The default value is zero
  def __init__(self, CheckingAccount = 0.0, SavingsAccount = 0.0):
    self._CheckingAccount = BankAccount(CheckingAccount)
    self._SavingsAccount  = BankAccount(SavingsAccount)
  
  # implementing the first method, deposit:  
  def deposit(self, amount, account) :
    if account == "C" :
      self._CheckingAccount.deposit(amount)
    elif account == "S" :
      self._SavingsAccount.deposit(amount)
      
  # implementing the second method, withdraw:
  def withdraw(self, amount, account) :
    if account == "C" :
      self._CheckingAccount.withdraw(amount)
    elif account == "S" :
      self._SavingsAccount.withdraw(amount)
      
  # implementing the third method, transfer - account indicates from which money is taken,
  # since the money transferred to the other account, we "deposit" them on the other account 
  # (f.ex. tranfser "C" --> withdraw from "C" & deposit on "S")
  def transfer(self, amount, account) :
    if account == "C" :
      self._CheckingAccount.withdraw(amount)
      if amount <= self._CheckingAccount.getBalance() :
        self._SavingsAccount.deposit(amount)
      elif amount > self._CheckingAccount.getBalance() :
        print ("Transfer sum exceeds the balance on the account. Penalty charged, transfer could not be completed.")
    elif account == "S" :
      self._SavingsAccount.withdraw(amount)
      if amount <= self._SavingsAccount.getBalance() :
        self._CheckingAccount.deposit(amount)
      elif amount > self._SavingsAccount.getBalance() :
        print ("Transfer sum exceeds the balance on the account. Penalty charged, transfer could not be completed.")
      
  # implementing the last method, getBalance:
  def getBalance(self, account):
    if account == "C" :
      print ("The Balance of the Checking Account is:", self._CheckingAccount.getBalance())
    elif account == "S" :
      print ("The Balance of the Savings Account is:", self._SavingsAccount.getBalance())

# Test
x = Portfolio(5000, 1000)
x.getBalance("C")
x.deposit(1000, "C")
x.transfer(6001, "C")
x.getBalance("C")
x.getBalance("S")
