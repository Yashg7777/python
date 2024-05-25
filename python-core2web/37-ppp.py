# public protected private 

'''
1) in python everything is public. 
2) access specifier types   == public , private , protected .

'''
#-----------------------------------------------
'''

class demo:
    z = 30                          #public

    def __init__(self):

        self._x=  10                #protected
        self.__y= 20                #private      #_demo__y

obj=demo()
print(obj._x)
# print(obj._demo__y)
print(obj.z)
'''
#----------------------------------------------
'''
class demo:

    z = 30

    def __init__(self):

        self._x = 10
        self.__y = 20

print(dir(demo))
obj = demo()
print(dir(obj))
'''
#---------------------------------------------- name angling
'''
class demo:
    def __init__(self):
        self.x=10
        self._y=20
        self.__z=30

print(dir(demo))

obj = demo()
print(obj.x)
print(obj._y)
print(obj.__z)
'''
#--------------------------------------------------
'''
class demo:
    def __init__(self):
        self.x=10
        self._y=20
        self.__z=30

print(dir(demo))

obj = demo()

print(dir(demo))

print(obj.x)
print(obj._y)
# print(obj.__z)     use _demo__z 

print(obj._demo__z)
'''

# -------------------------------------------------
'''
class demo:
    def __init__(self):
        self.x=10
        self._y=20
        self.__z=30

    def __fun(self):
        print("in fun funciton")

print(dir(demo))

obj = demo()

print(dir(demo))

print(obj.x)
print(obj._y)
# print(obj.__z)     use _demo__z 

print(obj._demo__z)

obj._demo__fun()           #function call.
'''
#------------------------------------------------

'''
class demo:
    def __init__(self):
        self.x=10
        self._y=20
        self.__z=30
        
    @classmethod
    def __fun(self):
        print("in fun funciton")

print(dir(demo))

obj = demo()

print(dir(demo))

print(obj.x)
print(obj._y)
# print(obj.__z)     use _demo__z 

print(obj._demo__z)

obj._demo__fun() 
demo._demo__fun()
'''

#------------------------------------------------

class demo:
    def __init__(self):
        self.x=10
        self._y=20
        self.__z=30
        
    @classmethod
    def __fun(self):
        print("in fun funciton")

obj1 = demo()
obj2 = demo()

print(obj1==obj2)

#   obj1.__eq__(obj2)

#--------------------------------------------------