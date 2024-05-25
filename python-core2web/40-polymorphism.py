#------------------------------------------------------------------------

'''                           POLYMORPHISM                                    '''
#-----------------------------------------------------------------------
'''

EKHADA FUN KIVA CLASS VEGLA VEGLA BEHAVE KARTA

'''
'''

1)METHOD OVERLOADING  

2)METHOD OVERRIDING

'''
#overriding

#duck type - run time object creation and decide to call which function
 
class demo:
    def fun(self):
        print("in demo : fun")

class memo:
    def fun(self):
        print("in memo : fun")

def callfun(obj):                                     # polymorphism
    obj.fun()

obj1 = demo()
obj2 = memo()

callfun(obj1)
#--------------------

class demo:
    def fun(self):
        print("in demo : fun")

class memo:
    def gun(self):
        print("in memo : gun")

def callfun(obj):                                     # polymorphism
    if obj == obj1:
        obj.fun()
    else:
        obj.gun()

obj1 = demo()
obj2 = memo()

callfun(obj2)

#------------------------

class demo:
    def fun(self):
        print("in demo : fun")

class memo:
    def fun(self):
        print("in memo : fun")

def callfun(obj):                                     # polymorphism
    if id(obj)==id(obj1):
        obj.fun()
    else:
        obj.gun()

obj1 = demo()
obj2 = memo()

callfun(obj1)

#-----------------------------------

class demo:
    def fun(self):
        print("in demo : fun")

class memo:
    def fun(self):
        print("in memo : fun")

def callfun(obj):                                     # polymorphism
    if hasattr(obj,"fun"):                            #duck type
        obj.fun()
    else:
        obj.gun()

obj1 = demo()
obj2 = memo()

callfun(obj1)

#------------------------------------- 

# duck type - run time 

x = "yash"
print(type(x))

x = []
print(type(x))


#--------------------------

#operator overloading

#------------

class demo:
    x = 10

class memo:
    x = 20

obj1 = demo()
obj2 = memo()

print(obj1 == obj2)

#------------

x = input()
y = input()
print(x +" "+ y )      # x.__add__(y)

x = 10 
y = 10.5
print(x + y )  

#=--------------------------------------------------------

                   #METHOD OVERLOADING#

#---------------------------------------------------------

def add(x,y=None,z=None):

    print(x+y+z)
    print(type(z))
    print(type(y))
# add(10,20,30)
# add(10)         
# add(10,20)





#---------------------------------------

# method over riding 😂😂

#---------------------------------------

class parent:
    def  property(self):
        print("gold,car,banglow")
    
    def career(self):
        print("engg")

class child(parent):

    def career(self):
        print("you tuber ") 
            # method override
    
obj = child()
obj.property()
obj.career()
