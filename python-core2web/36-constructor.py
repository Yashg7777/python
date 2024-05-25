'''
instance variable he constructor cha mdech initialize hota . pn apan ekhadi method pn write
karu shkto - instance method - tyat asnara varaible pn instance variable ch asto.
pn tya method la call karavach lagel tya instance varaible sathi ani jar tya method chi grj nsel tr
tila call kela janaar ch nhi pn conrtructor la call janar nahi as hot ch nahi
object create karavach lagel.

two ways 1) via constructor 2) instance method
'''
#--------------------------------------------------------------------------------


'''
class demo:
    def __init__(self):
        print("constructor")
        self.x=10
        self.y=20
    def setdata(self,z):
        self.z=z
    def printdata(self): 
        print(self.x)
        print(self.y)
        print(self.z)

obj=demo()        
# obj.printdata() -------will show attribute error as z is not initiallized.

'''

#--------------------------------------------------------------------------------
'''
class parent:
    def __init__(self):
        print("parent constructor1")
    def __init__(self):
        print("parent constructor2")

obj1=parent()
'''
#-----------------------------------------------------------------constructor--

'''        
class parent:
    def __init__(self):
        print("parent constructor1")
    def __init__(self):
        print("parent constructor2")

    
    def printdata(self):
        print("in fun1")
    def printdata(self):
        print("in fun2")

obj1=parent()
obj1.printdata()
'''
#-------------------------------------------------
#inheritance
#-------------------------------------------------
'''
class parent:

    def __init__(self):
        print("In Constructor")

    def parentfunc(self):
        print("In parent function")

class child(parent):
    def __init__(self):
        print("In Constructor child")              #constructor overriding

obj=child()
obj.parentfunc()

'''
#----------------------------------------

'''

class parent:

    def __init__(self):
        print("In Constructor")

    def parentfunc(self):
        print("In parent function")

class child(parent):
    def __init__(self):
        print("In Constructor child")    

    def childfunc(self):
        print("in child function")          

obj=child()
obj.parentfunc()
obj.childfunc()
'''
#-------------------------------------------

'''
class parent:

    def __init__(self):
        print("In Constructor")

    def parentfunc(self):
        print("In parent function")

class child(parent):
    def __init__(self):
        parent()                                    #change -create parent object-explicitly call
        print("In Constructor child")    

    def childfunc(self):
        print("in child function")          

obj=child()
obj.parentfunc()
obj.childfunc()
'''
#------------------------------------------------


'''
class parent:

    def __init__(self):
        print("In Constructor")

    def parentfunc(self):
        print("In parent function")

class child(parent):                           # child/subclass/derived class
    def __init__(self):
        super().__init__()                   #change - without creating object-parent/super/base
        print("In Constructor child")    

    def childfunc(self):
        print("in child function")          

obj=child()
obj.parentfunc()
obj.childfunc()

'''
#------------------------------------------------


'''
class parent:

    def __init__(self):
        print("In Constructor")

    def parentfunc(self):
        print("In parent function")

class child(parent):                           # child/subclass/derived class
    def __init__(self):
        parent.__init__(self)                   #change - without creating object-parent/super/base
        print("In Constructor child")    

    def childfunc(self):
        print("in child function")          

obj=child()
obj.parentfunc()
obj.childfunc()
'''

#-----------------------------------------------------------lecture 3 inheritance
'''
class parent:

    def __init__(self):
        print("in parent constructor")
        self.x=10
        self.y=20

    def dispdata(self):
        print(self.x)
        print(self.y)
class child(parent):
    pass

obj=child()
print(obj.dispdata)
'''
#--------------------------------------------------------------------33.15

'''   
class parent:

    def __init__(self):
        print("in parent constructor")
        self.x=10
        self.y=20

    def dispdata(self):
        print(self.x)
        print(self.y)
class child(parent):
    pass

obj=child()
obj.dispdata()

del obj                            #destructor- delete created object 

obj.dispdata()
'''

# garbage collector wait for call after deleting object.

#----------------------------------------------------------------------
'''
class parent:
    
    z=30  #change
    
    def __init__(self):
        print("in parent")

        self.x=5
        self.y=6
    
    def dispdata(self):

        print(self.x)
        print(self.y)
    
    @classmethod                     # created class method
    def dispParent(cls):
        print(cls.z)                 #class variable accessed

        #print(cls.x)  -cannot access as it is instance variable

class child(parent):
    pass

obj1=parent()         # obj for parent class
obj=child()           # obj for child class
obj.dispdata()        # created call for instance method
obj.dispParent()      # access parental class
parent.dispParent()   # calling class method

'''
#---------------------------------------------------
"""
destructor === notify that the object will get deleted.

__del__   method is called

destructor --notify
garbage collector --will delete object


1) when object will get deleted or will be deleted 
destructor will cae and tell us object will be deleted

2)it is not necessary to call destructor

def __del__(self):
    print("in destructor")

3) del obj ---- to delete the code.

"""

#-----------------------------------------------
'''
class parent:
    
    z=30  #change
    
    def __init__(self):
        print("in parent")

        self.x=5
        self.y=6
    
    def dispdata(self):

        print(self.x)
        print(self.y)
    
    @classmethod                     # created class method
    def dispParent(cls):
        print(cls.z)                 #class variable accessed

        #print(cls.x)  -cannot access as it is instance variable

    def __del__(self):
        print("in destructor")    # when work is complete then destructor will be called

obj=parent()
obj.dispdata()
obj.dispParent()

#obj.__del__()      calling destructor

del obj
'''

#---------------------------------------------

'''
class parent:
    
    z=30  #change
    
    def __init__(self):
        print("in parent")

        self.x=5
        self.y=6
    
    def dispdata(self):

        print(self.x)
        print(self.y)
    
    @classmethod                     # created class method
    def dispParent(cls):
        print(cls.z)                 #class variable accessed

        #print(cls.x)  -cannot access as it is instance variable

    def __del__(self):
        print("in destructor")

    
obj1=parent()    

# here 2 diff obj are created  and both will be deleted after the last line.                          ---change

obj2=parent()


print("the end")

'''
#-----------------------------------------


'''

In this code i have created 2 objects with the same name.
the objects within the class will get seperate space in memory except x and y object as they are same 

so when first oject is called and the execution is done the reference to that object is deleted 
and the obj1 reference is given to second object.'''


#---------------------------------
'''
class parent:

    def __init__(self):
        print("in parent")
        self.x=2
        self.y=2

    def dispdata(self):
        print(self.x)
        print(self.y)

    @classmethod
    def dispParent(cls):
        print(cls.z)
    
    def __del__(self):
        print("in destructor")

obj1=parent()                                 #obj1 -- will get dead and in distructor will get called
obj1=parent()                                 #obj2
print("the end")
'''
#----------------------------------------
'''
class parent:

    def __init__(self):
        print("in parent")
        self.x=2
        self.y=2

    def dispParent(self):
        print(self.x)
        print(self.y)

class child(parent):

    def __init__(self):

        self.x=30
        self.y=40
        super().__init__()     # x and y will be updated 
        

obj = child()
obj.dispParent()

'''
#------------------------------------
'''
class parent:

    def __init__(self):
        print("in parent constructor")
        self.x=2
        self.y=2

    def dispParent(self):
        print(self.x)
        print(self.y)

class child(parent):

    def __init__(self):
        print("In Child Constructor")
        super().__init__()       #change
        self.x=30
        self.y=40
             
        

obj = child()
obj.dispParent()
'''
#----------------------------------

'''
class parent:

    def __init__(self):
        self.x=20
        self.y=30

    def dispdata(self):
        print(self.x)
        print(self.y)

class child(parent):

    def __init__(self):
        self.x=30
        self.y=40

obj1=child()
obj1.dispdata()
'''
#------------------------------
'''
class parent:
    
    def __init__(self):
        self.x=20
        self.y=30

    def dispdata(self):
        print(self.x)
        print(self.y)

class child(parent):

    def __init__(self):
        self.x=30
        self.y=40
        super().__init__()

obj1=child()
obj1.dispdata()
'''
#----------------------------------------
'''

class parent:

    x=10
    y=20

    def dispdata(self):
        print(self.x)
        print(self.y)

class child(parent):
    
    x=30
    y=40
# output will be x = 30 and y = 40
obj1=child()
obj1.dispdata()

'''
#------------------------------------------------
'''

class parent:

    x=10
    y=20

    @classmethod
    def dispdata(cls):
        print(cls.x)
        print(cls.y)

class child(parent):
    
    x=30
    y=40

    @classmethod
    def dispdata(cls):
        print(cls.x)
        print(cls.y)

obj1=child()
obj1.dispdata()
'''
#---------------------------

'''
class parent:

    x=10
    y=20

    @classmethod
    def dispdata(cls):
        print("parent method")
        print(cls.x)
        print(cls.y)

class child(parent):
    
    x=30
    y=40

    @classmethod
    def dispdata(cls):
        print("child method")
        print(cls.x)
        print(cls.y)
        super().dispdata()

obj1=child()
obj1.dispdata()

'''
#--------------------------------27
'''
class xyz:
    z=30
    print("hello")       # it is not bind to class  ---- global method

    def __init__(self):
        print("constructor")


print("hey")
'''
#----------------------------------

'''
class demo:

    def __init__(self):

        print("in constructor")

print("start code")
obj=demo()
print("end code")
'''
#--------------------------------

'''

class demo:

    def __init__(self):

        print("in constructor")

print("start code")
obj=demo()
print("end code")

'''
#---------------------------
'''
class demo:

    print("start class")

    def __init__(self):

        print("in constructor")
    
    print("end class")

print("start code")
obj=demo()
print("end code")
'''

#-------------------------

'''class demo:

    x=10

    type(x)

    print("start class")

    def __init__(self):

        print("in constructor")
    
    print("end class")

print("start code")
obj=demo()
print("end code")'''

#------------------
'''

def fun():
    print("in nfun")
class demo:

    x=10

    type(x)

    fun()

    print("start class")

    def __init__(self):

        print("in constructor")
    
    print("end class")

print("start code")
obj=demo()
print("end code")

'''

#------------------
'''
class demo():

    def __init__(self):

        print("in constructor")

    def __del__(self):
        
        print("in destructor")

obj1=demo()
obj2=demo()

'''
#----------------------
'''
class demo():

    def __init__(self):

        print("in constructor")

    def __del__(self):
        
        print("in destructor")

obj1=demo()
obj2=demo()

obj3 = obj1

del obj1

print("end code")

'''
#-------------------

'''
class demo():

    def __init__(self):

        print("in constructor")

    def __del__(self):
        
        print("in destructor")


def fun():
    print("in fun")
    obj = demo()
    print("end fun")

fun()
print("end code")

'''
#----------------------------------
'''
class demo():

    def __init__(self):

        print("in constructor")

    def __del__(self):
        
        print("in destructor")


def fun():
    print("in fun")
    obj = demo()
    print("end fun")
    return obj

retobj=fun()
print("end code")

'''
#------------------------------

