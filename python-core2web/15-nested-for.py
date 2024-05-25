for i in range(1,20):
    if i % 3 == 0:
        if i%2==0:
            print(i,end=' ')
        else:
            print("*",end=' ')


for i in range(1,20):
    if i % 3 == 0:
        print("three")
    elif i % 5 == 0:
        print("five")
    else:
        print(i)
print("out of for loop ")




#nested for loop .

for i in range(3):
    print("In i for loop")
    
    for j in range(3):
        print("In j for loop")


#

for i in range(1):
    print("In i for loop ")

    for j in range(3):
        print("In j for loop ")

#

for i in range(2):
    print("in i for loop")

    for j in range(5):
        print("in j for loop ")


for i in range(3):
    print("in i for loop")

    for j in range(5,2,-1):
        print(f"in {j} for loop",end=" ")


        '''    1 - i 
               5 - j
               4 - j
               3 - j
               2 - j'''


for i in range(3):
    print("in i for loop")          

    for j in range(i):
        print("in j for loop")


'''  1 - i          in this loop we saw the indexing for inner loop as well as outer loop
     2 - i          so i = 0 will print i for outer loop while traversing for inner loop 
     3 - j          i=0 become i=0-1 = -1 then it will not print anything .
     4 - i          now for outer loop i=1 print i again and for innner loop i=1 become
     5 - j          i=1-1 = 0 so it print j for 0 not for 1 ok.
     6 - j          for i=2 it print i and then go for inner loop and print j twice for 0 and 1.
     '''


for i in range(3):
    print("In i for loop")

    for j in range(i+1):
        print("In j for loop")


''' 1 - i                   
    2 - j
    3 - i
    4 - j
    5 - j
    6 - i
    7 - j
    8 - j
    9 - j'''
#--------------------------
for i in range(3):
    for j in range(3):
        print("*",end=" ")
print()

#----------------------------

for i in range(3):
    for j in range(3):
        print("*",end=" ")
    


print()

#----------------------------


for i in range(3):
    for j in range(3):
        print("*",end=" ")
    print()

print()

#----------------------------

for i in range(2):
    for j in range(3):
        print("A",end = " ") 
    print()
#----------------------------
#print 1 to 9
    
num=1
for i in range(3):
    for j in range(3):
        print(num,end=" ")
    print()

print()

#---------------------------
'''111
   222
   333'''
num=1
for i in range(3):
    for j in range(3):
        print(num,end=" ")
    num += 1
    print()

print()

#---------------------------

'''123
   123
   123'''

num=1
for i in range(3):
    for j in range(3):
        print(num,end=" ")
        num += 1
    num=1
    print()

print()