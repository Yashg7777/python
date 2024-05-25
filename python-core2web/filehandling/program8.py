f1 = open("incubator.txt","w+")  # will erase old data

# f1 = open("incubator.txt","a+")  === will go further with old data

f1.write("mobile\n")
f1.write("back\n")
f1.write("front\n")
# print(f1.read())

f1.close()
# print(f1.read())



# modes

'''
r - file data read (file compulsury present) else= file not found err
w - file data write (file not present then it create one)
a - append is write at end of line 
r+ - read and write
w+ - write and read
a+ - append and read

x - write ( if file is present then push error,,everytime new file)

binary

rb
wb
ab
rb+
wb+
ab+


1) fileobj,seek(10)--- used to reach at particular location 
(11,0)-start of the file
(11,1)- current ----- for this the file should be binary file
(11,2) - eof - end of th file - foe this too binary file 
2) fileobj.tell() --- let us know where is the pointer


'''

'''
f1 = open("incubator.txt","r")

f1.seek(11,0) 

print(f1.read(10))

print(f1.tell())

print(f1.read(10))        

print(f1.tell())

print(f1.readline()) --- will read particular line only

print(f1.readlines()) --- will create a list with \n to show a particular line

print(f1.readline(3)) --- will get 3 character only

print(f1.readlines(3)) --- go with line but go until it go to \n and read upto it




'''