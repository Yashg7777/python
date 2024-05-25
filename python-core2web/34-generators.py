#===================================================================================================
# -----------------------------------GENERATOR----------------------------------------------------- 
# ==================================================================================================


'''
def fun():
    x=10
    y=10

    yield x
    yield y
p=fun()
for i in p:
    print(i)
'''

#------------------------------

'''
1)generator keep eye on stack .
2)keep process of function going after yeild method 
3) we are using yield instead of return .
4) freeze stack frame.
5) start executing line in code after leaving a particular line in function/ where is executed last time.
6) generator is iterator
7) when function return it return as generator 
8) python has 2 type of stack  1) normal stack frame 2) special stack frame for generator
9) next method is used to freeze and begin to execute next line 
10)generator keep the reference with help of flag to keep the reference. 
   when it become 0 it will leave reference
'''
#==============
'''
def fun():
    x=10
    print(x)
    x+=1
    print(x)
fun()
fun()
fun()

'''
#--------------

# here nothing will be output as it return generator's object.
'''
def fun():
    print("start fun")
    yield 10
    print("end fun")

fun()
'''
#-----------------
'''
def fun():
    print("start fun")
    #yield 10
    print("end fun")

print("start fun")
fun()
print("end fun")
'''
#------------------
# it become magic fun as it have yield which freeze stack frame
'''
def fun():
    print("start fun")
    yield 10
    print("end fun")

print("start fun")
fun()
print("end fun")
'''
#-------------------
#convert function to generator type and return it 

'''
def fun():
    print("start fun")
    yield 10
    print("end fun")

print("start fun")
ret=fun()

print(type(ret))
print(type(fun))
'''
#---------------------
'''
def fun():
    print("start fun")
    yield 10
    yield 20
    yield 30
    print("end fun")

ret = fun()

for i in ret:
    print(i)
'''
#----------------------
'''    
def fun():
    print("start fun")
    yield 10
    yield 20
    yield 30
    print("end fun")

for i in fun():
    print(i)
'''
#-------------------- here this fun will be simple fun as yield method is not present
# yield/generator is iterable
'''
def fun():
    print("start fun")
    # yield 10
    # yield 20
    # yield 30
    print("end fun")

for i in fun():
    print(i)
'''
#---------------------------------------------------------------------------------------
#--------------------- -----   1) next-used to iterate lines     2) yield
# next print next generator object/yield .

'''
def fun():
    print("start fun")
    yield 10
    yield 20
    yield 30
    print("end fun")


# for i in fun():       -   no end condition to stop or declare
#     print(i)

ret = fun()

print(next(ret))
print(next(ret))
print(next(ret))
# print(next(ret))   - show stop iterating as reached limit of yeild method == 3.

'''

'''
if use loop it will execute everything as iterates every line .
if using next method then will stop executing next line and left the code.'''
'''
normal function and generator function are same. when yield is present the function has ability
to pause the function and exit the function at that line. it can also return back to function
where it left the function and start executing next line onwards.  '''
#same as context switch
#generator freeze at yield.

#-----------------------------------------------------------------------------------------

'''
def fun(x,y):
    print("start while loop with (x=1 and y = 10)")
    while(x<=y):
        yield x
        x+=1
    print("\n end while loop")
for val in fun(1,10):
    print(val,end=" ")

'''

