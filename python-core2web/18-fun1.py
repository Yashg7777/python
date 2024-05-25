#function ----

'''1.make code readable
   2.make code less redundant
   3.used for less complexity
   4.DEF - this keyword is used to defination of function
   5.It required () for the function
   6.Once defined it can be called x time. '''


''' 1.NUMBER SYSTEM BASIC CODE----ARMSTRONG  STRONG  EVENODD ASCII SUMATION '''

def fun():
    print("in fun ")
print("started")
fun()
print("stopped")


'''1.PARAMETERS ARE USED TO STORE THE VALUES FOR ARGUMENTS 
   2.ARGUMENTS ARE PASSSED TO FUNCTION. '''

def sumTwo(a,b):
    ans = a + b
    print(ans)

x = int(input("Enter the value for x :"))
y = int(input("Enter the value for y :"))

sumTwo(x,y)
sumTwo(x+10,y+20)

#sum without function--------------------------


val = int(input("enter number:"))
sum = 0
for i in range(1,val+1):
    sum += i
print(sum)

#sum of n number code ------------------

def sumN(x):
    sum = 0
    for i in range(1,x+1):
        sum = sum + i
    print(sum)

val = int(input("Enter number :"))
sumN(val)

#divisible or not code --------------------

def div(x):
    if x%4==0 and x%5==0:
        print("number is divisible")
    else:
        print("number is not divisible")

val = int(input("Enter number :"))
div(val)


def playerinfo(jerNo,playerName):
    print("number on jersey ",jerNo," and name of player is ",playerName)
jr = int(input("enter jersey number :"))
name = input("enter player name :")
playerinfo(jr,name)


#RETURN STATEMENT--------------------


def add(a,b,c):
    return a+b+c
ans=add(10,20,10)
print(ans)



#factorial code ------------------
def fact(x):
    mul=1
    for i in range(1,x+1):
        mul *= i
    print(mul)

j = int(input("enter a number :"))
fact(j)


x=1234
y = str(x)
l = [int(i) for i in y]
print(sum(l))

a=input("enter:")
b=input("enter:")

print(a+b)





def fact(x):
    fact = 1
    for i in range (1,x+1):
        fact *= i
    return fact 

x=10
fact(x)