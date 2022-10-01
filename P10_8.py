"""
Implement a superclass Person. Make two classes, Student and Instructor, that inherit from Person. 
A person has a name and a year of birth. A student has a major, and an instructor has a salary. 
Write the class declarations, the constructors, and the __repr__ method for all classes. 
Supply a test program that tests these classes and methods.
"""

## The module defines the classes that model Person class
#

## A generic Person superclass
#
class Person :
  ## construct a person object with name and DoB.
  #  @param personName the person's name
  #  @param birthDate the date of birth of the person
  #
  def __init__(self, personName, birthDate) :
    self._personName = personName
    self._birthDate  = birthDate
    
  ## call the special method __repr__
  #  @return string representation of person's Name and Birth date
  #
  def __repr__(self) :
    return str(self._personName) + ", " + str(self._birthDate)
    
### The second class is the Student subclass with person superclass
class Student(Person) :
  ##  Construct a student subclass of person superclass
  #   @param personName the person's name (instance variable of superclass)
  #   @param birthDate  the person's birth date (--//--)
  #   @param studMajor  the student's major
  def __init__(self, personName, birthDate, studMajor):
    super().__init__(personName, birthDate)
    self._studMajor = studMajor
  
  ## call the special method __repr__
  #  @return string representation of student's Name and Birth date abd Major
  #
  def __repr__(self) :
    return "Student " + str(self._personName) + ", " + str(self._birthDate) + ". Major in " + str(self._studMajor)

### The last subclass is a Instructor
class Instructor(Person) :
  ##  Construct an instructor subclass of person superclass
  #   @param personName the person's name (instance variable of superclass)
  #   @param birthDate  the person's birth date (--//--)
  #   @param instWage   the instructor's salary
  def __init__(self, personName, birthDate, instWage):
    super().__init__(personName, birthDate)
    self._instWage = instWage
  
  ## call the special method __repr__
  #  @return string representation of Instructor's Name and Birth date and salary
  #
  def __repr__(self) :
    return "Instructor " + str(self._personName) + ", " + str(self._birthDate) + ". Salary: " + str(self._instWage)





per = Person("Adriana Luthik", "11 Sept 2000")
print("Expected: Adriana Luthik, 11 Sept 2000")
print(per)

stud = Student("Djimmy", "4 Oct 1995", "Business law")
print("Expected: Student Djimmy, 4 Oct 1995. Major in Business Law")
print(stud)

instr = Instructor("Frida", "31 Jan 1997", "1215000")
print("Expected: Instructor Frida, 31 Jan 1997. Salary: 1215000")
print(instr)


