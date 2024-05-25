# write operations


# f1 = open("core.txt","r+")   # read + write 

f1 = open("core.txt","w")       # erase old data and put new data

f1.write("go\n")
f1.write("ruby\n")

f1.close()