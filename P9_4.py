"""
Implement a class Address. An address has a house number, a street, an optional apartment number, a city, a state, and a postal code. 
Define the constructor such that an object can be created in one of two ways: with an apartment number or without. 
Supply a print method that prints the address with the street on one line and the city, state, and postal code on the next line. 
Supply a method def comesBefore(self, other) that tests whether this address comes before other when compared by postal code.
"""

class Address:
  # Constructor takes as input all characteristics/features of the address. 
  # To make a feature of the address optional we need to use None value that will allow to pass the address without apartment number
  def __init__(self, house_num, street, city, state, post_code, apart_num = None):
    self._house_num = house_num
    self._street    = street
    self._apart_num = apart_num
    self._city      = city
    self._state     = state
    self._post_code = post_code
    
    
  def show_address(self):
  # the desired outcome is the street name in the first line and city, state and postal code in the next line
    print (str(self._street) + str(self._apart_num) + "\n", str(self._city) + ", " + str(self._state) + ", " + str(self._post_code))

  def comesBefore(self, other):
  # since we can pass both str and int/float as input for postal code it is better to re-format all inputs to compare properly
    if float(self._post_code) > float(other._post_code):
      print ("The new address comes before previous one")
    else:
      print ("The new addres comes after previous one")
    
    
    
address1 = Address(55, "Harbitzalleen", "Lillestrøm", "Viken", 1975)
address1.show_address()
address2 = Address(23, "Trikkveien", "Oslo", "Akershus", "0930")
address1.comesBefore(address2)
