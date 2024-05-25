#wap to check number are divisible by 4 and 5
'''
def div(x):

    if x%4==0 and x%5==0:
        print(x , "is divisible by 4 and 5 ")
    else:
        print(x,"is not divisible by 4 and 5")


x=int(input("enter a number:"))
div(x)

'''

#wap to determine whether entered angles define a right angle triangle .
# take three vaues of angle from user.

'''
def right_angle_triangle(a,b,c):
    if a+b+c==180:
        if a==90 and b+c==90:
            print('right angle triangle at a')
        elif b==90 and a+c==90:
            print('right angle triangle at b')
        elif c==90 and b+a==90:
            print("right angle triangle at c")
        else:
            print("not right angle triangle")
    else:
        print("please check value of sum of angles is 180")




a=int(input("angle :"))
b=int(input("angle :"))
c=int(input("angle :"))
right_angle_triangle(a,b,c)

'''

#take two number from user and print the sum of those numbers if the sum is even
'''
def checkeven(x,y):
    sum=a+b
    if sum%2==0:
        print("{} is even".format(sum))
    else:
        pass
a=int(input("number a:"))
b=int(input("number b:"))

checkeven(a,b)

'''


#take a number from user and check whether it is present in list.if present print availabler
'''

def checklist(a):
    list1=[10,20,30,40,50]
    if a in list1:
        print("available")
    else:
        print("not availble")

a = int(input("enter a number:"))
checklist(a)

'''
#-----------------------------------------

'''
def checklist(a):
    list1=[10,20,30,40,50]
    for i in list1:
        if a in list1:
            print("available")
            break
    else:
        print("unavailable")

a = int(input("enter a number:"))
checklist(a)

'''
#print 'core2web' string a number of times entered by the 
# user if the number is even
'''
def numString(a,str):
    pass
    if a%2==0:
        for i in range(a):
            print(str)

str="Core2Web"
a=int(input("enter a number:"))
numString(a,str)

'''
#write a program to check that number is odd using if..

'''
def oddno(a):
    if a%2!=0:
        print("Odd")
    else:
        pass
a=int(input("enter a number:"))
oddno(a)

'''

#take 2 number frm user and check they are odd ,if odd print sum
'''

def oddSum(a,b):
    if a%2==0 and b%2==0:
        sum=a+b
        print(sum)
    else:
        pass
a=int(input("enter a number:"))
b=int(input("enter a number:"))
oddSum(a,b)

'''

#take a single characterr from user and cheack its ascii value is even if even print the character
'''
char=input('a character:')
if ord(char)%2==0:
    print(char)

'''

#take two character from user. check they are odd,if odd print sum of ascii value.
'''
char1=input('a character:')
char2=input('a character:')

if ord(char1)%2==0 and ord(char2)%2==0:
    sum=ord(char1)+ord(char2)
    print(sum)
else:
    pass

'''

#take a number from user,if divisible by 8 and remainder is 3 print the remainder
'''
a=int(input("enter a number:"))
b=3
if a % 8 == 3:
    print(b)

'''