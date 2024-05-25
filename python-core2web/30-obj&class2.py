class employee:

    def __new__(cls):
        print("hello")
        return object.__new__(cls)

    def __init__(self):
        print("world")

employee()

#---------------------------------------------
class Company:
    print("company")
    print(int(input("enter a number :")))

obj=Company()

#-------------

class company(object):
    pass
#---------------

class company(object):
    def disp(self):                          #<-this is method
        print("hello")
def fun():                               #<-this is function
    print("fun")

print("start fun")
fun()
obj=company()
obj.disp()
print("end code")

#---------------

class company(object):
    def disp(self):                       
        print("hello")
def fun():                             
    print("fun")

def disp():
    print("display")

print("start fun")
fun()
obj=company()
obj.disp()
print("end code")

#-----------------------

def fun(x):
    print("in fun")

def fun():
    print("in run")

fun()
fun(10)

#same name to function, it is object.
#override function
#return updated funntion



#----------------------

class company(object):
    def disp(self):
        print("hello")
print("start")
obj=company()
obj.disp()
print("end code")

#----------------------
'''





'''
#-----------------------
class employee:

    def __init__(self):
        print("in constructor")
        self.x=10
        self.y=20

    def disp(self):
        print(self.x)
        print(self.y)

obj=employee()

#---------------------------
#constructor
#---------------------------

#initializer

class demo:
    def __init__(self):
        print("in init")
demo()


#--------

class demo:
    def __init__(self):
        print("in init")
obj=demo()

#----------

class demo:
    def __init__(self):
        print("in init")
obj=demo()
print(obj)

#--------

#creator

class demo:
    def __new__(cls):
        print("memory allocate")
        return super().__new__(cls)
    
    def __init__(self):
        print("in init")

obj=demo()

#---------------

