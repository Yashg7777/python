'''if statement
   if elif else statement
   if else statement

   for loop
   while loop

   else suite
   break statememt
   continue statement
   switch statement
   pass statement
   assert statement
   return statement

   nested for 
   nested while

   '''

#if statement 

''' if(condition - true / false ) : 

- if condition is true then statement is exeuted - it is considered as true 
- if condition is false nothing will be output it is false 
- indentation is important to maintain the loop

when use if 
-when to check condition is true else it is not required     '''





# age = 19
# if(age > 18):
#     print("you are eligible for voting ")

# age1 = int(input("enter age :"))
# if(age1 > 18):
#     print("you are adult !")




num = int(input("enter the number :"))
if(num > 0 and num < 10):
    print("in if body ")
    print("number is natural !")

print(" out of if ")



# aged = int(input("enter yor age :"))
# if aged > 18 :                                    indentation is required --- body should be complete
# print("eligible for voting")
# print("out of if ")


#horizontal tab - indentation 
''' 1. give atleast 1 tab 
    2. you can give as many as you want for that after 1 tab 
    3. take as many vertical drop down .
    4. maintain the indentation'''



store = open
if(store == open ):
    print("you are welcome, have something you need ")

# pass - statement
    
'''1. if you want to run code without body ... but you also want to pass the condition.
   2. we use pass to run the code without error'''

age2 = int(input("enter age :"))
if(age2>18):
    pass
print("elegible for voting ")

print("out")



# syntax error for if 

'''if(age > 18 ) <- colon misssing error .........   syntax error
        print("eligible")              
        
        
    if(age > 19):    <- error resolved 
        print("eligible") '''



x = 10
y = 20
if(x):   #  <- x is given something --not 0 then it is true not a error in cpython .
    print("true")                                   #if check true/false condition in python
print("out of if")

