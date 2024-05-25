#code 1

'''
class parent:

    def marry(self):
        print("deepika")
    
class child(parent):

    def marry(self):
        print("alia")

obj = child()
obj.marry()
'''
# code 2

class parent:

    def marry(self):
        pass
    
class child(parent):

    def marry(self):
        print("alia")


obj = parent()
obj.marry()

# code 3


class parent:

    def marry(self):
        pass
    
class child(parent):

    def marry(self):
        print("alia")

obj =parent()
obj.marry()
obj1 =child()
obj1.marry()

#  types of class ---------------- abstract class(cant create object) , concrete class
from abc import ABC

class demo(ABC):
    def __init__(self):
        print("demo cha constructor")

demo()

# code 3

from abc import *

class demo(ABC):
    def __init__(self):
        print("demo cha constructor")

    @abstractmethod
    def fun(self):
        pass

demo()

#code 4

from abc import *

class demo(ABC):
    def __init__(self):
        print("demo cha constructor")

    @abstractmethod
    def fun(self):
        pass

demo()

# code 5

from abc import *

class hyundai(ABC):

    def __init__(self):
        print("the hyundai company")

    def slogan(self):
        print("slogan")

    @abstractclassmethod
    def cartype(self):
        pass

class suv(hyundai):

    def cartype(self):
        print("suv type")

class sedan(hyundai):

    def cartype(self):
        print("type sedan")

# print(type(ABC))

obj = sedan()
obj.cartype()


# abstract class is used when child class having changes with the methods.


from abc import *

class distributer(ABC):

    def __init__(self):
        pass

    @abstractclassmethod
    def store(self):
        pass

class faltanstore(distributer):

    print(" store in faltan")

    def store(self):
        print("rate of 1 pantshirt : 700")

class kothrudstore(distributer):

    print("the store at kothrud")

    def store(self):
        print("rate of pantshirt : 500")
    
class dekkan(distributer):

    print("store at dekkan ")

    def store(self):
        print("rate of pantshirt  : 900 ")
        

obj = dekkan()
obj.store()

#----------------

from abc import *

class mobile(ABC):

    def slogan(self):
        print("the era of cellphone")

    @abstractclassmethod
    def deviceName(self):
        pass

class vivo(mobile):


    def deviceName(self):
        print("The vivo company")
        print("vivo v29")

class mi(mobile):

    

    def deviceName(self):
        print("the xiomi company")
        print("redmi note 9")
        

class samsung(mobile):


    def deviceName(self):
        print("the samsung company")
        print("samsung s24 ultra")

obj = samsung()
obj.deviceName()


#code ------------


from abc import ABCMeta,abstractmethod

class hyundai(metaclass = ABCMeta):

    def slogan(self):
        print("dfjkbg")

    def cartype(self):
        pass
class verna(hyundai):

    def cartype(self):
        print("sedan")

class creta(hyundai):

    def cartype(self):
        print("suv")
    

obj = verna()
obj.cartype()
obj.slogan()


