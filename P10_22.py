#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implement a superclass Appointment and subclasses Onetime, Daily, and Monthly. An appointment has a
description (for example, “see the dentist”) and a date. Write a method occursOn(year, month, day)
that checks whether the appointment occurs on that date. For example, for a monthly appointment, 
you must check whether the day of the month matches. Then fill a list of Appointment objects with 
a mixture of appointments. Have the user enter a date and print out all appointments that occur on that date.
"""

## This module creates a code that stores appointments with description and date
#

## Superclass Appointment defines the general behavior of the class
#
class Appointemnt():
    ## Constructor containts one variable for description and three variables to capture the date
    #  @param description is a string that should be used to describe appointment
    #  @param year is used to specify the year of an appointment
    #  @param month is used to specify the month of an appointment
    #  @param day is used to specify the day of an appointment
    #
    def __init__(self, description, year, month, day):
        self._descript = description
        self._year     = int(year)
        self._month    = int(month)
        self._day      = int(day)
        
        
    ## The method works diferently depending on what subclass is invoked. 
    #  Therefore, I want here just to define abstract class
    #
    def occursOn(self):
        raise NotImplementedError
        
    ## I want to create and additional method to print description of appointment to use it in the end of the task
    #
    def getAppointment(self):
        return (self._descript)
        
        
## This subclass inherits from Appointment. The class creates the appointment that will not occur more than once
#
class Onetime(Appointemnt):
    ## The class uses the same initial values as superclass, nothing to change/add
    #  @param description is a string that should be used to describe appointment
    #  @param year is used to specify the year of an appointment
    #  @param month is used to specify the month of an appointment
    #  @param day is used to specify the day of an appointment
    #
    def __init__(self, description, year, month, day):
        super().__init__(description, year, month, day)
        
    ## To use occursOn() method properly we need to expand it. I want to return True if the condition is satisfied 
    #  to used it in the loop in the end of the task
    #  
    #  @param year is used to check whether the year of an appointment coincides
    #  @param month is used to check whether the month of an appointment coincides
    #  @param day is used to check whether the day of an appointment coincides
    #
    def occursOn(self, year, month, day):
        if self._day == int(day) and self._month == int(month) and self._year == int(year):
            print("The appointment takes place on the specified date")
            return True
        else:
            print("There is no appointments on that date")
    
## This subclass inherits from Appointment. The class creates the appointment that will not occur more than once
#
class Monthly(Appointemnt):
    ## The class uses the same initial values as superclass, nothing to change/add
    #  @param description is a string that should be used to describe appointment
    #  @param day is used to specify the day of an appointment
    #
    def __init__(self, description, day):
        super().__init__(description, "2022", "01", day)
        
    ## To use occursOn() method properly we need to expand it. It should return "positive match" if the day 
    #  of appointment coincides, therefore no need to check year or month. Therefore conditions check only day
    #  @params year and month are kept just to allow user pass them
    #  @param day is used to check whether the day of an appointment coincides
    #
    def occursOn(self, year, month, day):
        if self._day == int(day) :
            print("The appointment takes place on the " + str(day) +"th of each month")
            return True
        else:
            print("There is no appointments on that date")

## This subclass inherits from Appointment. The class creates the appointment that will not occur more than once
#
class Daily(Appointemnt):
    ## The class uses the same initial values as superclass, nothing to change/add
    #  @param description is a string that should be used to describe appointment
    #
    def __init__(self, description):
        super().__init__(description, "2022", "01", "01")
        
    ## To use occursOn() method properly in this case we need to modify it. 
    #  Since the daily appointment should repeat itself each day it there are no need to check any condition
    #  We keep all the parameters to allow user to pass them
    #
    def occursOn(self, year = "", month = "", day = ""):
        print("The appointment takes place every day")
        return True
        

# create list with miztures of objects
organizer = []
organizer.append(Onetime("Visit doc", "2022", "03", "07"))
organizer.append(Monthly("Lunch with grandma", "07"))
organizer.append(Daily("Meeting with my toothbrush"))
organizer.append(Onetime("Interview with BBC", "2023", "12", "31"))

# Create interface to type in the data and print all the appointments on that date
day   = input("Please, type in the day: ")
month = input("Please, type in the month using number: ")
year  = input("Please, type in the year: ")

output = []
for i in range(len(organizer)):
    if (organizer[i].occursOn(year, month, day)) == True:
        output.append(organizer[i].getAppointment())

print(output)






