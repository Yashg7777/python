#   PICKLE

# SERIALIZATION AND DESERIALIZARION

'''
pickle.demp(obj1,obj2);--- used to put this obj to file
pickle.load()---- to read ferom the file

'''

#------------------------------------------------------------------
# os.path.isfile
#------------------------------------------------------------------
'''
import os

if os.path.isfile("userdata.txt"):
    print("file present")
else:
    print("file ubsent")
'''

#---------------------
'''
import employee,pickle

f1=open("empdata.txt","wb")

empobj = employee.employee(12,"ashish",2.0)

pickle.dump(empobj,f1)
f1.close()
'''

#---------------

import employee,pickle

f1=open("empdata.txt","rb")

obj=pickle.load(f1)
obj.display()