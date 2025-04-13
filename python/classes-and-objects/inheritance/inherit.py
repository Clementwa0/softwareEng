# Inheritance allows us to define a -
# class that inherits all the methods and -
#  properties from another class.

# type of classes
#  parent class and child class

# parent class
class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        # object methods
    def printname(self):
        print(self.firstname, self.lastname)

# child class
class student(person):
    def __init__(self, fname, lname):
      person.__init__(self,fname,lname)  
# create object
x= student("Mike","Olsen")
# execute object
x.printname()

# super() function
class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
    # add properties
        self.gradyr = year
x = student("Mike","Olsen",2019)
print(x.gradyr)

# Adding methods
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome()