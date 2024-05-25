def fact(x):
    fact=1
    for i in range (1,x+1):
        fact *= i
    return fact 

x=10
fact(x)


#return multiple value from function

def add(a,b,c):
    a+=10
    b+=10
    c+=10

    return a,b,c
    
x=int(input("enter:"))
y=int(input("enter:"))
z=int(input("enter:"))
a,b,c=add(x,y,z)
print(a)
print(b)
print(c)


#python can return multiple due to tuple


def add(a,b,c):
    a+=10
    b+=10
    c+=10

    return a,b,c
    
x=int(input("enter:"))
y=int(input("enter:"))
z=int(input("enter:"))
hello =add(x,y,z)
for i in hello:
    print(i)



#parameter in function

def fun(x:int,y:int):
    print(x)
    print(y)

fun(50,80)
fun("yasha","yash")



def fun(x:int,y:int)->int:
    print(x)
    print(y)
    return "hello"

a=fun(50,80)
b=fun("yasha","yash")

print(a)
print(b)


#default parameter
def add(x,y,z=30):
    print(x)
    print(y)
    print(z)
    
add(10,20)

def add(x,y,z=30):
    print(x)
    print(y)
    print(z)
    
add(10,20,30)

def add(x,y,z=30):
    print(x)
    print(y)
    print(z)
    
add(10,20,30)