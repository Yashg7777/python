'''

-------------------------------------------------------------------------------------------------
=========================================INHERITANCE=============================================
-------------------------------------------------------------------------------------------------

'''
# parent class cha kahi functionalaties child class mde add hotat 

'''
# parent class
class company():
    pass

# child class
class employee():
    pass


instance variable
instance method
class variable
constructor
static method 
class method
new  

8791305527
''' 

class Company(object):

    x=10

    def __init__(self,compName,loc):
        self.compName=compName
        self.loc = loc
    

    def compInfo(self):
        print(self.compName)
        print(self.loc)

class Employee(Company):
    pass

obj1 = Employee("microsoft","pune")
obj2 = Employee("microsoft","bangalore")

obj1.compInfo()
obj2.compInfo()