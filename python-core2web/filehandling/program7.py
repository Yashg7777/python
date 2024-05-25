#append------

f1 = open("core.txt","a")

# print(f1.read())   cannot read a file with append

# f1.write("kanha")
friends = ["ashish\n","manish\n","ssatyam\n"]
f1.writelines(friends)