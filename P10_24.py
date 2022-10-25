#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Improve the appointment book program of Exercises P10.22 and P10.23 by letting the user save the appointment data to a file and reload the data from a file. 
The saving part is straightforward: Make a method save. Save the type, description, and date to a file. 
The loading part is not so easy. First determine the type of the appointment to be loaded, create an object of that type, 
and then call a load method to load the data.
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
        
    ## The method save should be created as abstract class since we need to save the type of each object
    #  
    def save(self):
        raise NotImplementedError
        
    ## The method load should be created as abstract class since we need to load the info after object is created
    #  
    def load(self):
        raise NotImplementedError
        
        
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
        
    ## To use occursOn() method properly we need to expand it. 
    #  
    #  @param year is used to check whether the year of an appointment coincides
    #  @param month is used to check whether the month of an appointment coincides
    #  @param day is used to check whether the day of an appointment coincides
    #
    def occursOn(self, year, month, day):
        if self._day == int(day) and self._month == int(month) and self._year == int(year):
            print("The appointment takes place on the specified date")
        #    return True
        else:
            print("There is no appointments on that date")
    
    ## Method save should save the type, description and date of an appointment to a file
    #  @param filename defines the file name that will be stored in cd if filepath is not specified
    #  @param write_or_append should be specified for a proper work of the method "w" for write and "a" for append
    #
    def save(self, filename, write_or_append):
        doc  = open(filename, write_or_append)
        text = "Onetime: " + self._descript + " " + str(self._year) + "/" + str(self._month) + "/" + str(self._day) + "\n"
        doc.write(text)
        doc.close()
        
    ## Method load should rewrite the data already stored in the object, tha task is a bit different to interpret, therefore,
    #  I assume we need first create an object with random data ("determine the type and create an object"), then we upload the correct
    #  data from the text-file and store it as correct values for all variables
    #  @param filename defines the file name that will be stored in cd if filepath is not specified
    #
    def load(self, filename):
        book =  open(filename, "r")
        content = []
        line = str(book.readline())
        content.append(line)

        while line != "":
            line = book.readline()
            content.append(line)
            
        for i in range(len(content)):
            if content[i].replace("/", " ").replace(":","").replace("\n","").split(" ")[0] == "Onetime":
                self._descript = " ".join(content[i].replace(":","").replace("\n","").split("/")[0].split(" ")[1:-1])
                self._year     = int(content[i].replace(":","").replace("\n","").split("/")[0].split(" ")[-1])
                self._month    = int(content[i].replace(":","").replace("\n","").split("/")[1])
                self._day      = int(content[i].replace(":","").replace("\n","").split("/")[2])
    
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
        #    return True
        else:
            print("There is no appointments on that date")


    ## Method save should save the type, description and date of an appointment to a file
    #  @param filename defines the file name that will be stored in cd if filepath is not specified
    #  @param write_or_append should be specified for a proper work of the method "w" for write and "a" for append
    #
    def save(self, filename, write_or_append):
        doc  = open(filename, write_or_append)
        text = "Monthly: " + self._descript + " " + str(self._year) + "/" + str(self._month) + "/" + str(self._day) + "\n"
        doc.write(text)
        doc.close()

    ## Method load should rewrite the data already stored in the object, tha task is a bit different to interpret, therefore,
    #  I assume we need first create an object with random data ("determine the type and create an object"), then we upload the correct
    #  data from the text-file and store it as correct values for all variables
    #  @param filename defines the file name that will be stored in cd if filepath is not specified
    #
    def load(self, filename):
        book =  open(filename, "r")
        content = []
        line = str(book.readline())
        content.append(line)

        while line != "":
            line = book.readline()
            content.append(line)
            
        for i in range(len(content)):
            if content[i].replace("/", " ").replace(":","").replace("\n","").split(" ")[0] == "Monthly":
                self._descript = " ".join(content[i].replace(":","").replace("\n","").split("/")[0].split(" ")[1:-1])
                self._year     = int(content[i].replace(":","").replace("\n","").split("/")[0].split(" ")[-1])
                self._month    = int(content[i].replace(":","").replace("\n","").split("/")[1])
                self._day      = int(content[i].replace(":","").replace("\n","").split("/")[2])        
        
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
    #    return True
    
    
    ## Method save should save the type, description and date of an appointment to a file
    #  @param filename defines the file name that will be stored in cd if filepath is not specified
    #  @param write_or_append should be specified for a proper work of the method "w" for write and "a" for append
    #
    def save(self, filename, write_or_append = "a"):
        doc  = open(filename, write_or_append)
        text = "Daily: " + self._descript + " " + str(self._year) + "/" + str(self._month) + "/" + str(self._day) + "\n"
        doc.write(text)
        doc.close()
    
    ## Method load should rewrite the data already stored in the object, tha task is a bit different to interpret, therefore,
    #  I assume we need first create an object with random data ("determine the type and create an object"), then we upload the correct
    #  data from the text-file and store it as correct values for all variables
    #  @param filename defines the file name that will be stored in cd if filepath is not specified
    #
    def load(self, filename):
        book =  open(filename, "r")
        content = []
        line = str(book.readline())
        content.append(line)

        while line != "":
            line = book.readline()
            content.append(line)
            
        for i in range(len(content)):
            if content[i].replace("/", " ").replace(":","").replace("\n","").split(" ")[0] == "Daily":
                self._descript = " ".join(content[i].replace(":","").replace("\n","").split("/")[0].split(" ")[1:-1])
                self._year     = int(content[i].replace(":","").replace("\n","").split("/")[0].split(" ")[-1])
                self._month    = int(content[i].replace(":","").replace("\n","").split("/")[1])
                self._day      = int(content[i].replace(":","").replace("\n","").split("/")[2])   
                
                
### Test Section ###
# Create text-file
app_one = Monthly("Coffe with mr.X", 16)
app_one.save("organizer.txt", "w")
app_two = Daily("Meeting with toothbrush")
app_two.save("organizer.txt", "a")
app_tre = Onetime("Meet Santa", "2022", "12", "25")
app_tre.save("organizer.txt", "a")

# create objects with randomly wrong data
app_one = Monthly(".", 0)
app_two = Daily("..")
app_tre = Onetime("...",0,0,0) 

# use method load to rewrite the data to correct data
app_one.load("organizer.txt")
app_two.load("organizer.txt")
app_tre.load("organizer.txt")        

# we use the occursOn method test to check whether the data was uploaded correctly. If yes the dates from the first part of test will return positive match
app_one.occursOn(2022, 1, 16)
app_two.occursOn()   
app_tre.occursOn(2022, 12, 25)
