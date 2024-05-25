'''
def fun(x,y=30):
    print(x+y)
fun(10)
'''
#--------------------------------------------------
'''
def compInfo(compName,empCount):
    print(compName,":",empCount)

compInfo('Microsoft',70000)
compInfo('Google',76000)
compInfo('Apple',78000)

compInfo(800,'core2web')
'''
#--------------------------------------------------

#NAMED ARGUMENT
'''
def compInfo(compName,empCount):
    print(compName,":",empCount)

compInfo('Microsoft',70000)
compInfo('Google',76000)>/-
compInfo('Apple',78000)

compInfo(empCount=800,compName='core2web')
'''
#--------------------------------------------------

#argc--- standard word.
#tuple is used for this 
#passing variable numberr of arguments to a function.----varargs
'''
def fun(*x):
    print(x)
    print(type(x))

    for i in x:
        print(i)
fun(10,20,30,40)
'''
#-------------------------------------------
'''
def fun(x,y,*argv):
    print(x)
    print(y)
    print(argv)

fun(10,20,30,40)
'''
#------------------------------------------
'''
def fun(x,y,*argv):
    print(x)
    print(y)
    print(argv)

fun(10,20) #empty tuple
'''
#------------------------------------------
'''
def fun(*argv,x,y):
    print(x)
    print(y)
    print(argv)

fun(10,20)#type error
'''
#------------------------------------------

#key-value pair in parameters------- using **argv
#dictionary
#key-word arguments
#passing variable number of keyword argument to a function
'''
def fun(**argv):
    print(argv)
    print(type(argv))

fun(x=10,y=20)'''

#--------------------------------------------------------------------
'''
def fun(x,y,z):
    print(x,y,z)

fun(10,y=20,z=12)
'''
#------------------------------------------------------------------

# def fun(**argv,x,y):  <--- show error cause it is dictionary
#     print(argv)
#     print(type(argv))

# fun(x=10,y=20)

#------------------------------------------------------------------
'''
def fun(**argv):
    for key,value in argv.items():
        print(key,":",value)
fun(x=10,y=12,p=14)
'''
#------------------------------------------------------------------



