# # compare two number and define which number is greater


# '''def max(x,y):
#     if x > y:
#         print(x," is greater")
#     else:
#         print(y," is greater")

# g=int(input("enter first number :"))
# h=int(input("enter second number :"))
# max(g,h)'''


# #check number is pos or neg or zero

# '''def fun(x):
#     if x > 0:
#         print("{} is positive number.".format(x))
#     elif x < 0:
#         print("{} is negative number.".format(x))
#     else:
#         print("{} number is zero.".format(x))


# val=int(input("enter a number :"))
# fun(val)'''

# #continue statement code

# '''
# fruits = ['apple','banana','cherry','drakshe','strawberry']

# for fruit in fruits:
#     if fruit == 'banana':
#         continue
#     if fruit == 'drakshe':
#         break
        
#     print(fruit)
# '''


# a = int(input('enter:'))
# a = a // int(input('enter :'))
# print(a)




# a,b,c=0,0,0
# a = input("enter:")
# b = input("enter:")
# c = input("enter:")
# list1 =[a,b,c]
# print(list1)

# for i in range(10,0):
#     print(i,end=' ')


# name = input('enter name:')
# for i in range(len(name)-1,-1,-1):
#     print(name[i])


# #unpacking of tuple.....
    
# fruits = ('apple','banana','cherry','raspberry','strawberry')

# (green,*tropic,red)=fruits

# # green,yellow,*red = fruits
# print(green)
# print(tropic)
# print(red)


# #set
  


# jersy_no =7
# print(jersy_no)
# print(type(jersy_no))


# x,y=10,16
# for i in range(x,y+1):
#     print(i)


# c=int(input("enter a number :"))
# d=int(input("enter second number:"))

# for i in range(c,d+1):
#     if i%2==0:
#         print("%d is even."%i)
#     else:
#         print("{} is odd.".format(i))

# print("hence we got it.")

# x=int(input(" "))
# i=1
# while x>=i:
#     print(x)
#     x-=1


# playerlist = ['rohit','shubhman','virat','shreyash']
# playername=input()



# for player in playerlist:
  
#     if player == playername:
#         print("%s player is present"%player)
        
#         break
# else:
#     print("is not present")


# numbers=[1,2,3,4,-6,5,6,7,4,9]

# neg=False
# count=0
# for num in numbers:
#     if num <0:
#         neg=True
#         print("found",num)
#         break
#     count+=1
  
# if neg == False:    
#     print("not found")

# print(count)


# fruits=['mango','apple','banana','cherry','chiku']
# fruitname=input("enter name of fruit you want to search: ")
# found=False

# for fruit in fruits:
#     if fruit == fruitname:
#         print("fruit is present")
#         found=True
#         break
# if not found:
#     print("not present")



# #-----------------------------------
# for i in range(3):
#     for j in range(3):
#         print("*",end=" ")
#     print()

# for i in range(3):
#     for j in range(3):
#         print("*",end="* ")
#     print()
     

# def fun():
#     print("in fun")
# print("start")
# fun()
# print("stop")
# #----------


# employee = ['rohit','satyam','aniket','siddharth','yash','pankaj']

# print(employee)
# print(type(employee))
# print(type(employee[0]))

# employee = [{10,'rohit'},{20,'satyam'},{30,'aniket'},{40,'siddharth'},{50,'yash'},{60,'pankaj'}]
# print(type(employee[0]))

# player=[{18:'virat'},{45:'rohit'}]
# print(type(player[0]))



# list=[i for i in range(1,10)]
# print(list)

# even=[i for i in range(1,11) if i % 2 == 0]
# print(even)



# player1={45:'rohit',18:'virat',7:'dhoni'}
# print(player1)
# print(type(player1))

# print(player1.get(18))
# print(player1.values())
# print(player1.keys())

# for key,value in player1.items():
#     print(key," : ",value)

# print(player1.pop())
# print(player1.popitem())

#-------

# sets={20,30,40,50,30,60,23,45}
# set1={3,4,5,6,7}


#-------------------

string='hello yash'
print(string.capitalize())

#-----------------

def outer():
    def inner():
        print("in inner fun")
    inner()
    print("in outer")
print("start")
outer()
print("stop")

#----------------

def outer(x,y):
    def inner():
        print("inner")
    
    print("outer")
    return x,y

retval=outer(10,20)
print(retval)

for i in retval:
    print(i)

#----------------------------
'''    
def outer(x,y):
    def inner():
        print("inner")
    print("in outer")
    print(id(inner))
    return inner

retobj=outer(10,20)
print(id(retobj))
retobj()
'''

#----------------

def outer(x,y):
    def inner(a,b):
        print("in inner fun")
        return a+b
    print("in outer")
    print(x+y)
    return inner

retobj=outer(5,6)
innerret=retobj(2,3)
print(retobj)
print(innerret)

#--------------------------
def outer():
    def inner(x,y):
        print("in inner1 fun")
        return x+y
    def inner1(a,b):
        print("in inner1 fun")
        return a*b
    
    return inner,inner1

inner,inner1=outer()

ret1=inner(2,3)
ret2=inner1(3,4)
print(ret1+ret2)
print(ret2)
print(ret1)


#---------------------------

a,b = map(int,input().split())
b,c,d = map(int,input().split())
e,f,g = map(int,input().split())

print("enter the numbers you want to :",a,b,c,d,e,f,g)


#----------


A, B = input().split()
C, D, E = input().split()
F, G, H, I = input().split()
print(A, B, C, D, E, F, G, H, I)

a,b,c = input().split()
print(a,"\n",b,"\n",c)

#-----------
'''
Write a program in the IDE which does the following
Accepts the count of test cases - 
t - as an integer input given in the 1st line.
This is followed by
t lines - Each line contains an integer 
For each test cases, prints out the integer 
N to console on a separate line'''

t = int(input())

for i in range(t):
    n=int(input())
    print(n)



'''
Lets write a program in the IDE which performs the following The 1st line of input is an integer 
t - the count of test cases Each test case consists of 2 lines of input
The 1st line of input has 2 space separated integers - accept them as variables 
A and B The 2nd line of input has 3 space separated integers - accept them as variables 
C, D and E For each test case - output all integers on a single line'''

t = int(input())       

for i in range(t):     
    
    A,B = map(int,input().split())
    
    # accept 3 integers on the 2nd line using map
    C,D,E = map(int,input().split())
    
    
    # output the 5 integers on a single line for each test case
    print(A, B, C, D, E)


dict1 ={"banana":"yellow","apple":"red","grape":"black"}
print(type(dict1),len(dict1),id(dict1))

dict1["grape"] = "green"
print(dict1)
dict1['pineapple']= 'yellow'
print(dict1)