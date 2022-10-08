""" Add a class MultiChoiceQuestion to the question hierarchy of Section 10.1 that allows multiple correct choices. 
The respondent should provide all correct choices, separated by spaces. Provide instructions in the question text.
"""

##   This module defines a class that models exam questions.
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

# the module constructs a MultiChoiceQuestion class
# the class will allow question to have multiple correct choices
# the respondent should provide all correct choices, separated by spaces
class MultiChoiceQuestion(Question) :
    # intialize instance variables, for question text we can use the same value as for superclass
    # for answer we need to use an empty list
    #
    def __init__(self):
        # call the superclass constructor to invoke its instance variables
        # add an instance variable _choices as an empty list. Will be used to store the choices
        # add an instance variable _correct as an empty string. It will be used to generate a string with numbers of right options
      super().__init__()
      self._choices = []
      self._correct = str()

    ## Adds an answer choice to this question.
    # @param choice the choice to add
    # @param correct True if this is the correct choice, False otherwise 
    # 
    def addChoice(self, choice, correct) :
        self._choices.append(choice) 
        if correct :
        # the program will add a correct option to empty string from instance variable _correct 
        # Convert len(choices) to string to capture the number of correct option 
            self._correct = self._correct + " " + str(len(self._choices))
            self._correct = self._correct.strip()
            self.setAnswer(self._correct)

    ## Expand Question.display()    
    def display(self) :
        # Display the question text
        super().display()
        # Display the answer choices
        for i in range(len(self._choices)) :
            choiceNumber = i + 1
            print("%d: %s" % (choiceNumber, self._choices[i]))

### Test the program
def main():
    first_q = MultiChoiceQuestion()
    first_q.setText("Choose an olympic champion in marathon:")
    first_q.addChoice("E. Kipchoge", True)
    first_q.addChoice("N. Chavkin", False)
    first_q.addChoice("S. Kiprotich", True)
    first_q.addChoice("J. Ingebrigtsen", False)

    presentQuestion(first_q)

def presentQuestion(q):
    q.display()
    response = input("Your Answer: ")
    print(q.checkAnswer(response))

main()