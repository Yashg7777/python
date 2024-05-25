'''In Python programming, a "flag" is a boolean variable that is used to indicate whether
   a certain condition has been met.
   
   Flags are commonly used in programming to control the flow of logic in a program.
    
   They help in making decisions based on whether certain conditions are true or false. 
'''

'''A flag is usually initialized to False or 0 '
   (depending on whether you're using boolean or integer flags).

   As your program executes, you might encounter certain conditions where you need to 
   remember that something happened or to signify that a condition has been met.

   When the condition is met, you set the flag to True or 1.

   Later in your code, you can check the state of the flag to determine whether 
   the condition occurred.'''


numbers = [2, 3, -5, 7, 8]

# Initialize the flag
negative_found = False

# Iterate through the list
for num in numbers:
    if num < 0:
        negative_found = True
        break

# Check the flag
if negative_found:
    print("The list contains negative numbers.")
else:
    print("The list does not contain negative numbers.")


#check fruit is present or not .
fruits = ["mango","apple","banana","cherry","chiku"]
fruit = input("enter name :")

found = False
count=0
for fr in fruits:
    if fr == fruits:
        print("fruit is present .")
        found = True
        break

if not found:
    print(fruit," is not present.")


playerlist = ["rohit", "shubhman", "virat", "iyer", "dhoni"]
playername = input("Enter name of player: ")

found = False  # Flag to track if player is found

for player in playerlist:
    if player == playername:
        print(playername, "present in list.")
        found = True
        break

if not found:
    print(playername, "is not present in the list.")

