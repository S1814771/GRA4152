"""
Implement a class ComboLock that works like the combination lock in a gym locker, as shown here. 
The lock is constructed with a combination — three numbers between 0 and 39. 

The reset method resets the dial so that it points to 0. The turnLeft and turnRight methods turn the dial by a given number of ticks to the left or right. 
The open method attempts to open the lock. The lock opens if the user first turned it right to the first number in the combination, 
then left to the second, and then right to the third.
"""
class ComboLock :
  def __init__(self):
    self._dial = 0
    
  def ComboLock(self, secret1, secret2, secret3) :
# to set the combination to lock the locker    
# the secret number could have values between 0 and 39, furthermore from the task text, we see that the second secret is lower than first since we need to turn the dial to the left
    if secret1 >= 0 and secret1 <= 39 and secret2 >= 0 and secret2 <= 39 and secret3 >= 0 and secret3 <= 39 and secret1 > secret2 and secret3 > secret2:
      self._secret1 = secret1
      self._secret2 = secret2
      self._secret3 = secret3
    else: print("The secret must be between 0 and 39, and the first and third secret must be bigger than the second secret")
  
  def reset(self) :
    #the method sets the dial to zero, and reset the stored values for combinations used to open the locker
    self._dial     = 0
    self._attempt1 = 0
    self._attempt2 = 0
    self._attempt3 = 0
    print("The dial at zero. You have to begin from scratch to find all the three secrets")
    
  def turnLeft(self, ticks) :
    # Since to open the locker we need to turn the locker right-left-right we can store the first secret after we call the turnLeft method
    self._attempt1 = self._dial
    # Assumption: by turn to left I mean turn to the lower number
    if self._dial - ticks >= 0:
      self._dial = self._dial - ticks
    else:
      print ("Please, do check the number of ticks, your desired number of ticks results in the secret smaller than zero")
    
  def turnRight(self, ticks) :
    # Since to open the locker we need to turn the locker right-left-right we can store the second secret after we call the turnRight method. 
    # The correct number will be stored after we call turnRight for the second time
    self._attempt2 = self._dial
    # Assumption: by turn to left I mean turn to the higher number
    if self._dial + ticks <= 39:
      self._dial = self._dial + ticks
    else:
      print ("Please, do check the number of ticks, your desired number of ticks results in the secret bigger than 39")
    
  def open(self) :
    # Since we try to open the locker when the dial is on the position of the last secret we store its value first
    self._attempt3 = self._dial
    if self._secret1 == self._attempt1 and self._secret2 == self._attempt2 and self._secret3 == self._attempt3:
      print ("Your combination is correct, the locker is unlocked")
    else:
      print ("Wrong combination, please use reset method and try again")
  
  # For proper functionality of the class we need to add extra methods to indicate the dial's position
  def getValue(self):
    print ("The value of the dial is: ", self._dial)



# The right scenario
x = ComboLock()
x.getValue()
x.ComboLock(22,21,22)
x.turnRight(22)
x.turnLeft(1)
x.turnRight(1)
print("Expected: Locked should open")
x.open()

# The wrong scenario
x = ComboLock()
x.getValue()
x.ComboLock(20,2,7)
x.turnRight(22)
x.turnLeft(1)
x.turnRight(1)
print("Expected: Locked should not open")
x.open()
