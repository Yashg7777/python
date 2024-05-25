'''

attribute error
name error 
type error
syntax error
value error
range error
intendation error
key error
unbound error
assertion arror
overflow error

exception handling:::::

syntax error::: intendation ,

exception:::

1) error    2) syntax


'''

#syntax error
'''

def fun()   <------------------invalid syntax as : is not present
    print("hello")
fun()

'''
#intendation error-- compile time error
'''
def fun():
    print("helko")
        print("hel")    #<- intendation error
print("start code")
fun()

'''
#type error = missing 1 required positional argument ---runtime exception
'''
def fun(a,b):
    print(a)
    print(b)

print('start code')
fun(10,20)
fun(10)
print("end code")

'''

#TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''
def fun(a,b):
    print(a+b)
  

print('start code')
fun(10,20)
fun(10,'kanha')
print("end code")

'''

#AttributeError: 'demo' object has no attribute 'gun'. Did you mean: 'fun'?
'''
class demo:
    def __init__(self):
        print("helo")
    
    def fun(self):
        print("in fun")

obj = demo()
obj.fun()
obj.gun()     #< gun ---- not defined

'''
#NameError: name 'fun' is not defined

'''
class demo:
    def __init__(self):
        print("helo")
    
    def fun(self):
        print("in fun")

obj = demo()
fun()
'''
#AttributeError: 'NoneType' object has no attribute 'gun'
'''
class demo:
    def __init__(self):
        print("helo")
    
    def fun(self):
        print("in fun")

obj = demo()
obj.fun()

obj = None
obj.gun()

'''

#IndexError: list index out of range
'''
list1 = [ 10,'ashi',20,'mshi']

print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])

'''

#key error
'''
players = {18:'virat',45:'rohit'}
print(players)
print(players[45])
print(players[1])
'''

#-----------------------------------------------------------------52 -- examplee with 2 file

print("start code")

empid = 10
name = "kanha"

try:
    ans = empid + name
except:
    print("exception handled")
print("end code")



# exception handling lecture 2 --------===============================😂😎😛

print("Start Code")

num1 = int("Enter a value for num1 : ")
num2 = int("Enter a value for num2 : ")

print(num1 + num2)

print("End Code")

# for this code we need two try-except



# generic exception handling



# simple code 1

print("Start Code")

try:

    num1 = int(input("Enter a value for num1 : ")) 
except ValueError:
    print("please enter int value")

print("end code")


#---------------------code 2

print("Start Code")

try:

    num1 = int(input("Enter a value for num1 : ")) 
    num2 = int(input("Enter a value for num2 : ")) 
except ValueError:
    print("exception handling")
try:

    print(num1+num2)
except NameError:
    print("exception handling")
print("end code")

# code 3 ------------------------------------

list1 = [10,"kanha",20,"rahul",30]

try:
    index1 =int(input("enter a value for index :"))
    print(list1[index1])

    index2 = int(input("enter value for index :"))
    print(list1[index2])


    add =list1[index1]+list1[index2]

except ValueError:
    print("value err handled")

except IndexError:
    print("value err handled")

except TypeError:
    print("value err handled")
else:
    print(add)
print("end code")


#-----------------------------------------------------RAISE EXCEPTION

class VotingError(Exception):

    def __init__(self,msg):
        super().__init__(msg)

def voting(name,age):

    if age<18:
        raise VotingError("not eligible for voting")
    else:
        print("thanks for voting")

print("start code")

name= input("enter your name :")

try:
    age=int(input("enter your age :"))
except ValueError:
    print("proper integer value add kr")
    age=int(input("enter your age"))



try:
    voting(name,age)
except VotingError as err:
    print(err)

print("end code")