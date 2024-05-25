#....................................Nested Function.....................................................
'''
def outer():


    def inner1():
        print("In inner1 function")
    
    def inner2():
        print("In inner2 function")
    
    print("In outer function")

    inner1()
    inner2()
    

outer()
'''
#----------------------------------------------------------------------------
'''
def outer():


    def inner1():
        print("In inner1 function")
    
    inner1()
    inner2()  <---------------     unbound local error 

    def inner2():
        print("In inner2 function")
    
    print("In outer function")

outer()
'''

#----------------------------------------------------------------------------
'''
print("function")
def outer():

    def inner1():
        print("In inner1 function")

    def inner2():
        print("In inner2 function")
    
    print("In outer function")

outer().inner1()  <--------------------function  , in outer fun ...attritube error
'''
#------------------------------------------------------------------------


                                #   FUNCTION LECTURE 2    #
#===========================================================================
'''
def outer():
    def inner():
        print("in inner fun")
    inner()
    print("in outer fun")

print("start")
outer()
print("stop")
'''
#-----------------------------------------  46 min lecture 2
'''
def outer():

    def inner1():
        print("In inner1 function")

    def inner2():
        print("In inner2 function")
    
    print("In outer function")

outer()'''
#inner1()<---- it will not see inner functions until it visit outer function body --show name error 

#-----------------------------------------------
#error part ------

''' 
In python ...at compile time it check syntactical error only and at this stage 
nothing will get executed and syntax error: invalid syntax will be given

'''

'''
In python ...after compilation if there is any logical error....at this stage 
everything will print until that line of error is reached . then it will display the error

'''

'''
1.for function first off all body is required for outer function
2.it only enter to inner function when outer is called
3.once it is called it will call inner function sequentially
4.for inner function .. the function should be declared first 
5.the calling function should be after the body of inner function
6.the calling for inner function --should be in outer fun body.

'''



#--------------------------------------------
'''
def outer(x,y):
    def inner():
        print("In inner function")
    print("In outer function")
    return x,y

retval=outer(10,20)
print(retval)

for i in retval:
    print(i)
'''
#--------------------------------------------

# name of function is object -----------------------------------imp

'''
1. if you want to access a inner function from outer function 
   go with return inner    <<---- this will return address of inner function.
   
   call the function with   retobj()
   lets go through code'''

#----------------\

#FUNCTION RETURN A FUNCTION ==============================================================
'''
def outer(x,y):
    def inner():
        print("In inner function")
    print("In outer function")
    print(id(inner))
    return inner

retobj=outer(10,20)
print(id(retobj))
retobj()

'''
#----------------------------------------------
'''
def outer(x,y):
    def inner(a,b):
        print("In inner function")
        return a+b
    print("In outer function")
    print(x+y)
    return inner

retobj=outer(5,8)
innerret=retobj(2,3)
print(retobj)               <--return the address of inner
print(innerret)             <--print value returned by a+b
'''
#------------------------------------------
'''
def outer():
    
    def inner(a,b):
        sum=a+b
        print(sum)
        print("In inner1 ")
    
    def inner1():
        print("In inner2")

    return inner,inner1

retobj,retobj2 =outer()
retobj(12,34)
retobj2()


'''

#------------------------------------------------------

# METHODS 

#------------------------------------------------------

#method 1 

'''
def outer():
    def inner():
        print("iiner")
    def inner1():
        print("dfigh")

    return inner,inner1


inn1,inn2=outer()
inn1()
inn2()
'''
#-------------------------------------------------

# method 2
'''
def outer():
    def inner():
        print("iiner")
    def inner1():
        print("dfigh")

    return inner,inner1


retobj=outer()

for i in retobj:
    i()
'''
#-------------------------------------------------
'''
def outer():
    def inner1(x,y):
        print("inn inner1 loop")
        return x+y
    
    def inner2(a,b):
        print("inn inner2 loop")
        return a*b
    
    return inner1,inner2

inn1,inn2=outer()

ret1 = inn1(2,4)
ret2 = inn2(3,4)

print(ret1+ret2)
print(inn1)
print(inn2)

print(ret1)
print(ret2)
'''
#--------------------------------------------------
'''
def outer():
    def inner(x,y):
        print("inner1")

    return inner
    print("in outer")   <-- unreachable statement ,return will exit fun.

retobj=outer()
retobj(2,2)
'''

#--------------------------------------------------