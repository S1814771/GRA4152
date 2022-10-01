"""
Modify the checkAnswer method of the Question class so that it does not take into account different spaces or upper/lowercase characters. 
For example, the response "GUIDO van Rossum" should match an answer of "Guido van Rossum".
"""
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
    response     = response.lower().replace(" ","")
    right_answer = self._answer
    right_answer = right_answer.lower().replace(" ","")
    return response == right_answer
  
  ## Displays this question. 
  #
  def display(self) :
    print(self._text)


