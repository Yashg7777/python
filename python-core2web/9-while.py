# while loop

# i = 1
# while i < 5 :   '''iteration will not stop until increment is given '''
#     print(i)

    #i++ ---- not valid do i+=1 is valid

x= int(input("enter value for x :"))
i = 1
while(i<x+1):
    if(i%5==0):
        print(i)
    i+=1

# i=1
# while i<5:
#     print(i)
#     i+=1

# print(i)   

''' it will print 5 cause after print it will go to while again to check condition 
                before going to while it goes through print so print 5 as i
                 
                  
    1.when using while remember to give increment 
    2.check the increment indentation is with if loop
     '''
#-----------------------------------------


i = 1

x = int(input("enter value x:"))

while(i < x+1):

    if i % 5 == 0:
        print(i)
    
    i+=1

#------------------------------------------

num1 = int(input("enter num: "))
while num1 > 0 :
    print(num1)
    num1 -= 1

#---------------

x=10
while (x>0):
    print(x)

    x-=1
    if (x==5):
        break

#-------------

playerlist=['rohit','shub','virat','dhoni','sachin']
pname=input("enter name :")
for player in playerlist:
    if player == pname:
        print("present in list")

#-------------

playerlist=['rohit','shub','virat','dhoni','sachin']
pname=input("enter name :")

count=0

for player in playerlist:
    if pname == player:
        print("present in list")

        break
    count+=1

print(count)