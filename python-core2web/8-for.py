# # 1.range - is a class in python used in for loop 

# for x in range(5):
#     print("python ",end='')
#     print(x)                        #print from 0 to 4

# for x in range(5):   
#     print("python")


# for x in range(1,5,1):   #start from 1st element given to second last element
#     print(x)

# for x in range(4,5):   #started from 4 and end ata 4 
#     print(x)


# #step in python
    
# for x in range(10,5,-1):
#     print(x)


# '''range is a class in python which contain 3 carier - (10,4,6) 

#    range(5)- this is stop parameter     range(5,10)-start and stop parameter
#    range(5,4,3)-start ,stop , step 
   
#    (start-from 0,stop- stop is omitted ,step)
   
#    start is inclusive 
#    stop is exclusive'''


# for x in range(1,15,3):  # step by 3 - start from 1 , 4 , 7 , 10 , 1 3 
#     print(x)

# #user kadun 2 input x , y x =10 y=20  - print x from 10 to 20 and print to y 

# x=int(input("enter value of x :"))

# y=int(input("enter value of y :"))

# for i in range(x,y+1):
#     print(i)

# for i in range(10,3,-2):
#     print(i)

#take 2 input from user and print odd and even number from it 
    
w=int(input("enter first no :"))

e=int(input("enter second no :"))

# for i in range(w,e+1):
#     if(i%2==0):
#         print("{} is even number.".format(i))
#         print(i,"is even")
#         print("%d is even"%i)
#     else:
#         print("{} is odd number.".format(i))

#take 2 user input  from 1 to 100 ------ print number divisible by 4 and 5 by same number

# for i in range(w,e+1):
#     if(i%4==0 and i%5==0):
#         print("{}".format(i))


#3-litte bit logic

for i in range(1,5):
    print(i)

print(i) 
