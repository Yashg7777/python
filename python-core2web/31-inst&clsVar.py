
'''

types of variable 
1) class varaible
2) instance variable

types of method
1)class method
2)instance method/object method
3)static method

1.in emptty class --- new and init are always present
2.variable writren in constructor is called as INSTANCE VARIABLE
3.when class is created a namespace is created called CLASS NAMESPACE contain class variable and class methods
4.when object is created then namespace is called as instance namespace/object namespace.
5.namespace is folder for address.

6.method written into __init__ is called as INSTANCE METHOD.


'''
#---------------------

# same data for both objects 

class employee:

    def __init__(self):
        print("In Constructor")
        self.name="chandu"
        self.roll=23

    def empinfo(self):
        print(self.name)
        print(self.roll)

emp1=employee()
emp2=employee()
emp1.empinfo()
emp2.empinfo()

#----------------------
class employee:

#class variable
    
    company='facebook'                                     

#constructor-initializer
    
    def __init__(self):
        print("In Constructor")
        self.name="chandu"
        self.roll=23

#instance method
        
    def empinfo(self):
        print(self.name)
        print(self.roll)

#object created
        
emp1=employee()
emp2=employee()

#method called

emp1.empinfo()
emp2.empinfo()

#---------------------------------------------------------------------
# constructor and instance variables.



class employee:

    def __init__(self,name,roll):
        print("In Constructor")
        self.name=name
        self.roll=roll

    def empinfo(self):
        print(self.name)
        print(self.roll)

emp1=employee("monkey",15)
emp2=employee("aniket",13)

emp1.empinfo()
emp2.empinfo()

#-------------------------------------

class employee:

    def __init__(self,empId,empName):
        print("in constructor")
        self.empId=empId
        self.empName=empName
    def empInfo(self):
        print(self.empName)
        print(self.empId)

emp1=employee(12,"ani")
emp2=employee(16,"mnky")

emp1.empInfo()
emp2.empInfo()

#-----------------------


class employee:

    def __init__(self,empId=0,empName="ashi"):
        print("in constructor")
        self.empId=empId
        self.empName=empName
    def empInfo(self):
        print(self.empName)
        print(self.empId)

emp1=employee(12,"ani")
emp2=employee(16,"mnky")
emp3=employee()

emp1.empInfo()
emp2.empInfo()
emp3.empInfo()


#without using method

class employee:
    def __init__(self):
        print("in constructor")
        self.empId=12
        self.empName="kanha"
emp1=employee()
emp2=employee()

print(emp1.empId)
print(emp1.empName)

#attribute error will be shown---attribute error
print(employee.empId)      
print(employee.empName)


#------------------------------------------------------------------------
# CLASS VARIABLE / STATIC VARIABLES
#------------------------------------------------------------------------

class company:
    #class variable 
    compName="facebook" 

    def __init__(self):
        print("in constructor")
        self.empId=12
        self.empName="aniket"
    def compInfo(self):
        print(self.empId)
        print(self.empName)


    #   print(compName) - name error - compname is not defined 
        #this will fetch class variable
        print(company.compName)  
       
    
emp1=company()
emp1.compInfo()

#-------\

class company:
    compname ="facebook"

    def __init__(self):
        print("in constructor")
    
    #instance method
    def compInfo(self):
        print(self.compname)

emp1=company()
emp1.compInfo()
print(emp1.compname)
print(company.compname)

###
emp1.compname="meta"

emp1.compInfo()
print(company.compname)