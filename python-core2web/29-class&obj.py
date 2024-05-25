'''class employee:
    name ="kanha"
    empId =22
    sal =1.5

    def work(self):
        print("frontend dev")
    
obj =employee()
obj.work()
'''


print("Let's learn 'python' together with MySlate Team")

a = input()
l = len(a)
b = input()

if len(a)==1:
  print("0000",a)
  
elif len(a)==2:
    print("000",a)
elif len(a)==3:
    print("00",a)
elif len(a)==4:
    print("0",a)
elif len(a)==5:
    print(a)
else:
    print(a)


num1=input()
num2=input()

print(f"{int(num1):05d}")
print(f"{int(num2):>3}")

x=int(5)
print(type(x))

x='hello'[0]
print(x)



#----------------w3schools---------------

# class person:
#     name="yash"
#     occupation="student"
#     networth=10

# a=person()
# a.name="shubham"
# print(a.name,a.occupation)

# b=person()
# a.name="simba"
# print(a.name,a.occupation)
'''
class employee:
    def __init__(self,name,id) :
        self.name=name
        self.id=id
        print(name,id)

class programmer(employee):
    def lang(self):
        print("python")

e=employee("yash",420)
j=employee("ani",410)
 '''

 #------------------------
'''
class person:
    def __init__(self,name,age):    #init function called automatically
        self.name=name
        self.age=age
    
p1=person("john",36)
print(p1.name)
print(p1.age)
'''
#--------------------__str__ function---------------

#without str function
'''
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("john",36)
print(p1)
'''
#with str function

class person:
    def __init__(self, name, age):
        self.name=name 
        self.age=age
    
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = person("john",36)
print(p1)

#methods in objects -

'''objects also contain methods. methods in obj are functions
that are belong to object.'''

#lets create a method

class person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
    def fun(self):
        print("hello"+ self.name)
p1=person("john",46)
p1.fun()

#----

class program:
    def __init__(silly,name,age):
        silly.name=name
        silly.age=age
    
    def __str__(silly):
        return f"{silly.name}({silly.age})"
    def fun(abc):
        print("sg")

p1=program("yash",36)
print(p1)
p1.fun()







#====================================================================================
'''                    ~~~~~~~~~~~ core2web ~~~~~~~~~~~~~                         '''
#====================================================================================

#object class is parent class of every class 
'''
class employee(object):
    pass
'''
class employee:
   
    name ="kanha"         #<-------class variable
    empid= 22             #instance variable are in constructor in python
    sal = 1.5             #constructor is used to construct our requirement ---used to initialize instance varable.
    

    def work(self):
        print("frontend dev")
 
obj=employee()  
obj.work()



#----------------------

class employee:
    
    def __new__(cls):
        print("creator")
        return object.__new__(cls)

    def __init__(self):
        print("constructor")

employee()

#-----------------using super()----keyword

class employee:
    
    def __new__(cls):
        print("creator")
        return super().__new__(cls)

    def __init__(self):
        print("constructor")

employee()