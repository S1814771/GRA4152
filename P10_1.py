"""
Add a class NumericQuestion to the question hierarchy of Section 10.1. 
If the response and the expected answer differ by no more than 0.01, then accept the response as correct.
"""

### This part is taken from book
#   This module defines a class that models exam questions.
#

## A question with a text and an answer. 
#
class Question :
  ## Constructs a question with empty question and answer strings. 
  #
  def __init__(self) :
    self._text = "" 
    self._answer = ""
  
  ## Sets the question text.
  # @param questionText the text of this question 
  #
  def setText(self, questionText) :
    self._text = questionText
  
  ## Sets the answer for this question.
  # @param correctResponse the answer
  #
  def setAnswer(self, correctResponse) :
    self._answer = correctResponse
  
  ## Checks a given response for correctness.
  # @param response the response to check
  # @return True if the response was correct, False otherwise 
  #
  def checkAnswer(self, response) :
    return response == self._answer
  
  ## Displays this question. 
  #
  def display(self) :
    print(self._text)

### The end of the part taken from the book.     
    
### For the task we need to add a  new class to the Question hierarchy
#   I want to initialize an answer with value of zero, 
#   that will kind of similar to have a empty string as an initial value for answer of Question class
class NumericQuestion(Question):
  def __init__(self):
    super().__init__()
    self._answer = float("0.00")
  
  ## Here I want to allow to use both string, int, float as an answer format and convert it to float inside the loop
  #  In this way, value passed in function as "1.0" or 1 or 1.0 will work
  def checkAnswer(self, responce):
    if abs(float(responce) - self._answer) <= 0.01:
      print("Correct answer")
    else:
      print("Wrong answer")
  
  
  
  
  
  
  
  
  
  
  
  
  
