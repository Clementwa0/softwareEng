# object constructor

# create a class using class keyword
class Myclass:
    x = 5
# print(Myclass)

# create object name P1

obj = Myclass()
print(obj.x)

# _init_() function

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
#  _str_ fucntion
    def __str__ (self):
        return f"{self.name}({self.age})"
#  object methods 
    def myfunc(self):
     print("Hello my name is " + self.name)
     p1.myfunc()

# create a object
p1 = person("John", 36)
# delete objects
del p1.age

# modifying objects
p1.age=40

print(p1.name)
print(p1.age)
print(p1)