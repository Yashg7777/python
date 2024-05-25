'''

f1 = open("incubator.txt","r")

f1.seek(-10,2)  # to go for last 10 char-io.UnsupportedOperation: can't do nonzero end-relative seeks

print(f1.read())

'''
#-------------------
'''
f1 = open("incubator.py","wb")

f1.write("mobile")
f1.write("web")
f1.write("backend") #TypeError: a bytes-like object is required, not 'str'

f1.close()

'''

#---------------------------
'''
f1 = open("incubator.txt","w")

f1.write("mobile")
f1.write("web")
f1.write("backend")    # simple opertation performed to write

f1.close()
'''
#-------------------------------------------------------------------
'''
f1 = open("incubator.txt","rb")  # read file in binary mode 

#utf 8 -- unicode text format

print(f1.read()) 
f1.close()
'''
#--------------
'''
f1 = open("incubator.txt","rb")

print(f1.read().decode("utf-8"))

f1.close()

'''


#-----------------------
'''
f1 = open("incubator.txt","rb")

f1.seek(-10,2) 

print(f1.read().decode("utf-8"))
'''

#----------------------
'''
f1 = open("incubator.txt","rb")

f1.seek(-10,2) 

print(f1.read().decode("utf-8"))

f1.seek(-10,1)

print(f1.read().decode("utf-8"))

'''

#-=----==-=-=-=-=-=-=-=-=--=-=-=-=-----

