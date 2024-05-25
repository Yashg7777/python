#get a number as user input and print it until its value become i 

x=int(input("enter a number :"))
i = 1

while(x >= i ):
    print(x)
    x -= 1



y=int(input("enter a number :"))
while(x>0):
    print(x)
    x -= 1



c=int(input("enter a number :"))
for i in range(c,0,-1):
    print(i)


#given value of d=10 , now you have to print d until it become i ...but you have to stop at d=6..without break statement
d=int(input("enter a value :"))
while(d>0):
        if(d>=6):
            print(d)
            d -= 1




e=int(input("enter a value :"))
while(e > 0):    
    print(e)
    e = e-1

    if(e == 5):
        e = 0





#using break statement 
        
f=int(input("enter a value :"))
while(f > 0):    
    print(f)
    f = f-1

    if(f == 5):
        break;



j = int(input("Enter a value: "))
while j > 0:
     # Decrement j by 1 in each iteration to eventually exit the loop
    for i in range(j,5,-1):
        print(i)
    j-=1
   

j = int(input("Enter a value: "))
for j in range(j, 0, -1):  # Iterating j from its initial value down to 1
    pass  # You can put your desired logic here, or remove pass if no additional logic is needed
for i in range(10, 5, -1):  # Iterating from 10 down to 6
    print(i)



#example of using break statement :
    

playerlist = ["rohit","shubhman","virat","iyer","dhoni"]
playername=input("enter name of player :")

count = 0

for player in playerlist:
    count += 1 
    if player == playername:
        print(playername,"present in list.")
        break 
print("player is at position :",count) 







playerlist = ["rohit","shubhman","virat","iyer","dhoni"]
playername=input("enter name of player :")

for player in playerlist:
    
    if player == playername:
        print(playername,"present in list.")
        break 
    else:                                                             #repeated output will be given
        print("not present")


# to overcome with this go with next file ---- else suit
        



#using flag


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











            
    