# for pattern code nested for can be used 

''' for better pattern understanding must requiew best knowledge of 


if
if else
for
while
break
continue
assert'''




x = 4
for i in range(x):
    print("*",end=' ')

x= int(input("enter value :"))
for i in range(1,x+1):
    print(i,end = ' ')


x= int(input("enter value :"))
for i in range(x):
    print(i+1,end = ' ')


# x = 15      ---x= int(input("enter value :"))
x=int(input("enter numbeer :"))
for i in range(1,x):
    if i%2==0:
        print(i,end = ' ')
for i in range(1,x):
     if i%2!=0:
          print(i,end=' ')



x=int(input("enter numbeer :"))
for i in range(2,x,2):
        print(i,end = ' ')


# x =10 ----------> 1*3*5*7*9*



#using while 

x=int(input("enter number :"))
i=0
while i < x:
    i +=1
    if i%2==0:
        print(i,end=' ')
    else:
        print("*",end=' ')


# x = 50  ----.>>> 5 * 15 * 25 * 35 * 45 *
        
x=50

for i in range (5,x+1,5):
    if i%2==0:
        print("*",end=' ')
    else:
        print(i,end=' ')
    


# what is git ?? how to push codes to git ??? --- version control system.
        

# pattern questions 
    
'''***
   ***
   ***'''

for i in range(3):
    for j in range(3):
        print("*",end=" ")
    print()


'''** ** **
   ** ** **
   ** ** **'''

for i in range(3):
    for j in range(3):
        print("*",end="* ")
    print()

x=1
for i in range(5):
    for j in range(5):
        print(x,end=" ")
        x+=1
    print()
print()

#----------------------------

'''123
   234
   345'''

num=1

for i in range(3):
    num=i+1
    for j in range(3):
        print(num,end=" ")
        num += 1
        
    print()


'''understand 
   i=0 ----num=0+1=1  in j -  1,2,3
   i=1---num=1+1=2 in j 2,3,4
   i=2---num=2+1=3 in j 3,4,5'''
#------------------------------

for i in range(3):
    num = i
    for j in range(3):
        print(num+1,end=' ')
        num+=1
    print()

'''
    i=0   num=0 in j --0+1=1 ,2,3
    i=1   num=1 in j --1+1=2 ,3,4
    i=2   num=2 in j --2+1=3 ,4,5   
'''

#--------------------------------
'''123
   246
   369'''
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="")
    print()  

''' logic =--
    
    i will begin from 1 
    j will begin from 1
    
   0 1 2 3      -column j
   1 1 2 3
   2 2 4 6
   3 3 6 9    
   
   i*j for each matrix position
   
   '''



#----------------------------

'''*
   * *
   * * * '''




for i in range(3):
    for j in range(i+1):
        print("*",end=' ')
        
    print()
#-----------------------------------
    
'''1
   2 3
   4 5 6'''
num=1
for i in range(3):
    for j in range(i+1):
        print(num,end=' ')
        num+=1
    print()

#=-------------------------------

'''a
   a b 
   a b c'''

num=65
for i in range(3):
    for i in range(i+1):
        print(chr(num),end=' ')
        num +=1
    print()

#---------------------------
    
'''1 2 3
   4 5
   6'''
rows=int(input("enter rows : "))
num=1
for i in range(rows):
    for j in range(rows-i):
        print(num,end='   ')
        num+=1
    print()





#==========================
    
