# read and write 
fileobj = open("core.txt","r")

print(fileobj.read())

fileobj.seek(0)    # go back to 1st line again after reaading a file

print(fileobj.read())
