#if-elif-else

num = int(input("enter a number :"))

if(num>0):
    print("{} is positive number. ".format(num))
elif(num==0):
    print("{} is 0.".format(num))
else:
    print("{} number is negative.".format(num))



number = int(input("enter a number between 1 to 10 :"))
num1 = number*number

print("The square of number entered is : ",num1,end=" ")
if(num1%2==0):
    print("and %d is even." %num1)
else:
    print("and %d number is odd. "%num1)






