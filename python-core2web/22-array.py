''' ARRAY

array is class ------------------------


1.multiple emelemt collection
2.similar types of data can stored
3.index is given to each element
4.index start from 0
5.index access--multiple ways'''
'''

import array as arr     #<<<  import module 

jerNo=arr.array('i',[45,77,18,1] )   #<<<  create a function of array.(  ) <-put datatype for function #typecode
                                     #<<< colleciton is iterators , array=function arr= module 
                                     # i = datatype  typecode(datatype)
                                     # dynamic array --- 

'''
#---------------------ways to import array----------------------

#import array as arr 

#from array import *
 
#import array 

#---------------------------------------------------------------
'''
import array as arr

jerno=arr.array('i',[45,30,18,1,2])

print(jerno)
'''
#----------------------------------------------------
'''
import array as arr

data=arr.array('b'[-45,24,180,-18])

print(data)
'''
#---------------------------------------------
'''
import array as arr

data=arr.array('h'[-45,32767,180,-18])

print(data)
'''

#---------------------------
'''
import array as arr

data=arr.array('i'[-45,32767,180,-18])

print(data)
'''
#------------
'''
import array as arr

data=arr.array('h'[-45,32767,180,-18])

print(data)

'''
#--------------------------

# typecode==== b,h,i,l,q     ----- built in array   ------predefined array 

''' in python there is not a string array '''


#------------------array function's----------------------------------------------



#---------------------------------------------

'''
import array as arr

name =arr.array('u',['R','o','h','i','t'])
print(name)
'''
#---------------------------------------------

''' 1.append()
    2.buffer_info()
    3.byteswap()
    4.count()
    5.extend()
    6.list()
    7.index()
    8.insert()
    9.pop()
    10.remove()
    11.reverse()
    12.tolist()
    13.tobytes()'''


#-------------------------------------------------------------
'''
import array as arr

data = arr.array('i',[10,20,30,40,50])
data.append(60)                           #10 20 30 40 50 60
data.buffer_info()                        # <- address of element in array(address,length)
data.count()                              # counnt has parameter-- repreent occurence of element in ary
data.extend([70,80])                      # enter more than one value to add
data.index(400)                           # index
data.insert(4,500)                        
data.pop()
data.remove()
data.reverse()
data.tolist()


print(data.buffer_info())
print(id(data))                          # address of pointer

for i in data:
    print(i)
'''
#---------------------------------
'''   

import array as arr
listdata =[10,20,30,40]

arrdata = arr.array('i',[100,200,300,400])
print(arrdata)

arrdata.fromlist(listdata)
print(arrdata)            #100 200 300 400 10 20 30 40

'''
#--------------------------------------

#ARRAY SLICING

import array as arr

arrdata = arr.array('i',[10,20,30,40,50])
for i in arrdata[1:8]:
    print(i)
#------------------------------------\

a=int(input("a :"))
b=int(input("b :"))
c=int(input("c :"))

for i in range(a,b,c):
    print(i)

#-------------------------------------\
    
import array as arr

data=arr.array('h'[-45,32767,180,-18])

print(data)