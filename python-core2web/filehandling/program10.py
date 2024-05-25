# take input from user until he say's no
'''
f1 = open("userdata.txt","w")

while True:

    data = input("enter data : ")
    f1.write(data)
    f1.write("\n")


    boolval = input("want to write more data?(y/n)")

    if boolval == 'n':
        break

'''
# copy data from one file to another file
'''
f1 = open("userdata.txt","r")
f2 = open("maang.txt","w")

maang =f1.readlines()

for company in maang:
    f2.write(company)

f1.close()
f2.close()
'''

# --------------------

'''
print("start code")
try:
    f1=open("userdata.txt","r+")
    print(f1.read())
except FileNotFoundError:
    print("file not found")

f1.write("apple")

print("end code")

'''

#----------------------- 
'''
we opened a file for certain operation but sometime we dont know when to close 
that particular file at that time we use with

'''

#with statement
'''
with open("userdata.txt","r+") as f1:
    print(f1.read())

f1.write("meta")
'''



