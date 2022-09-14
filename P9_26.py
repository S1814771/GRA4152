"""
Design a Customer class to handle a customer loyalty marketing campaign. 
After accumulating $100 in purchases, the customer receives a $10 discount on the next purchase. Provide methods:
  - def makePurchase(self, amount)
  - def discountReached(self)
Provide a test program and test a scenario in which a customer has earned a discount and then made over $90, but less than $100 in purchases. 
This should not result in a second discount. Then add another purchase that results in the second discount.
"""

class Customer:
  def __init__(self, initial_balance = 0):
    self._balance = initial_balance
  
  def makePurchase(self, amount):
  # since the task does not us to keep counting the total spending I will concentrate on keeping the track of required amount to earn discount
  # to make it more observable I want to print the current status and eventually price of purchase with discount
  # after achieved discount I subtract $100 to make calculations of the next discount easier
    if self._balance >= 100:
      self._balance = self._balance + (amount - 10)
      print("Discount is used, the price of your purchase is: $", str(amount-10))
      self._balance = self._balance - 100
      print("To earn the next discount, you have to spend $", str(100-self._balance))
    else:
      self._balance = self._balance + amount
      
  def discountReached(self):
    if self._balance >= 100:
      print ("Discount achieved. The current balance is: $", self._balance, ". You will get a $10 discount on your next purchase")
    else:
      print ("Discount is not achieved. The current balance is: $", self._balance)

    
customer1 = Customer()
customer1.makePurchase(50)
customer1.makePurchase(55)
customer1.discountReached()
customer1.makePurchase(95)
