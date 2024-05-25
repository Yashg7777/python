'''

class Demo:
    x=10

    def __init__(self):
        self.y=20

    def disp(self):
        print(self.y)
        print(self.x)
        print(Demo.x)
    
obj1=Demo()
obj1.disp()

'''
#-------------------------------------------------------
# @- is a decorator 
'''
1)function decorator

'''
'''
def outer():
    print("in outer")

    def inner():
        print("in inner")

    inner()
outer()
'''
#-----------------------------
'''
def outer():
    print("in outer")

    def inner():
        print("in inner")

    return inner
obj=outer()
obj()

'''
#---------------------------
'''
def outerfun():
    print("in outer fun")

    def innerfun1():
        print("in inner fun1")
    
    def innerfun2():
        print("in inner fun2")

    innerfun1()
    innerfun2()

outerfun()
'''
#---------------------------
'''
def outerfun():
    print("in outer fun")

    def innerfun1():
        print("in inner fun1")
    
    def innerfun2():
        print("in inner fun2")

    return innerfun1,innerfun2


ret1,ret2=outerfun()
ret1()
ret2()

obj=outerfun()
for i in obj:
    i()
'''
#---------------------------- passing fun as parameter / argument----
'''    
def run():
    print("in run")
def fun(x):
    x()
    print("in fun")

fun(run)
'''
#-----------------------decorator chaining----------
'''
def gun():
    print("in gun")

def run(y):
    print("in run")
    y()
def fun(x):
    x()
    print("in fun")

fun(run(gun))
'''

#-------------------------getting step by step
'''
def decorfun(func):
    def wrapper():
        print("start wrapper")
        func()
        print("end wrapper")
    
    return wrapper

def normalfun():
    print("hello in normal function")

ret = decorfun(normalfun)
ret()
'''
#--------------------------------------------------
'''
def decorfun(func):
    def wrapper():
        print("start wrapper")
        func()
        print("end wrapper")
    
    return wrapper

def normalfun():
    print("hello in normal function")

normalfun = decorfun(normalfun)
normalfun()
'''
#--------------------------------------------------
'''
def decorfun(func):
    def wrapper():
        print("start wrapper")
        func()
        print("end wrapper")
    
    return wrapper

def normalfun():
    print("hello in normal function")

#normalfun = decorfun(normalfun)
normalfun()
'''
#-------------------------------------------------
'''
def decorfun(func):
    def wrapper():
        print("start wrapper")
        func()
        print("end wrapper")
    
    return wrapper

@decorfun
def normalfun():
    print("hello in normal function")

#ret = decorfun(normalfun)
normalfun()

'''
#-------------------------------------------------

'''
def decorfun(func):
    def wrapper():
        #print("start wrapper")     decorfun will be present in background but not well known to front user
        func()
        #print("end wrapper")
    
    return wrapper

@decorfun
def normalfun():
    print("hello in normal function")

#ret = decorfun(normalfun)
normalfun()

'''

#--------------------------------------------------------
#variable number of arguments
'''
def normalfun(*args):
    sumdata = 0

    for i in args:
        sumdata=sumdata+ i
    return sumdata

print(normalfun(10,20,30))

'''
#key word arguments
'''
def normalfun(**args):
    sumdata = 0

    for k,v in args.items():
        sumdata = sumdata + v
    return sumdata

print(normalfun(x=10,y=20,z=30))

'''
#-----------------------------------------------------------
#stepss
'''
def decorfun(func):
    def wrapper():
        print("start wrapper")
        func()
        print("end wrapper")
    
    return wrapper

def normalfun(x,y):
    print("In normal function")
    return x+y

print(normalfun(10,20))
'''
#-----------------------------------------------------------
'''
def decorfun(func):

    print("In decor function")

    def wrapper(*args):

        print("start wrapper")
        val = func(*args)
        print("end wrapper")
        return val
    
    return wrapper

@decorfun
def normalfun(x,y):
    print("In normal fun")
    return x+y

print(normalfun(10,20)) 
'''
#normalfun=decorfun(normalfun)----wrappper fun return
#print(decorfun(normalfun(10,20)))
# normalfun(10,20)---normal fun  return 


#abstract factory design pattern
     


#-------------------------------------------------------------------
# decorator chaining 
#-------------------------------------------------------------------
'''


def decorfun(func):
    
    def wrapper():
        print("Start wrapper2")
        func()
        print("End wrapper2")

    return wrapper
 
def decorrun(func):

    def wrapper():
        print("Start wrapper1")
        func()
        print("End wrapper1")

    return wrapper

@decorfun
@decorrun
def normalfun():
    print("In normal function")


# normalfun=decorfun(decorrun(normalfun))     <- code flow to check ...imp
normalfun()


'''


#------------------------------------------------------------------------------------

