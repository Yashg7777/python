#datatype in python
#there are 7 types of datatypes


#NUMERIC
# INT FLOAT COMPLEX

#BOOLEAN
# BOOL

#SEQUENCE
# STRING LIST TUPLE RANGE 

#SET
# SET

#MAPPING
# MAP : dict

#NONE 
# NONE

#BYTE
# BYTES BYTEARRAY


#numeric types -------------  

empId = 20
print(empId)
print(type(empId))         #<class 'int'>

jerNo = 45
print(jerNo)               #45
print(type(jerNo))         #<class 'int'>


#float types ---------------

price = 23.50
print(price)
print(type(price))

data = 34.45456465667543565456
print(data)                 
print(type(data))          #<class 'float'>

#complex types ---------------

complexdata = 10 + 10j
print(complexdata)
print(type(complexdata))


#boolean type ----------------

data = True
print(data)
print(type(data))

data2 = False
print(data2)
print(type(data2))


u = 10
t = 20
print(u == t)

ans = u + t
print(ans)


#sequence type ---------------

#string

'''string in python is written in three way'''

# way-1
friend1 = 'ani'
print(friend1)
print(type(friend1))

# way-2
friend2 = "anii"
print(friend2)
print(type(friend2))

# way-3
friend3 = '''pratik'''
print(friend3)
print(type(friend3))

# there is no char datatype in python , it is considered as string
wing = 'a'
print(wing)
print(type(wing))

#list

proLang = ["c","cpp","java","python"]
listData = [18,7,45,1,'virat','dhoni','dhoni','kl','ro']

print(proLang)
print(listData)

proLang[2] = 'shami'
print(proLang)


'''-duplicate data is allowed in list
   -list is mutable'''

#tuple

proLangt = ("c","cpp","java","python")
listDatat = (18,7,45,1,'virat','dhoni','kl','ro')

print(proLangt)
print(listDatat)

''' -tuple is immutable-data cannot canged'''

#range

ran = range(10)
ran1 = range(19,30)

for i in ran:
    print(type(ran))
    print(i)


#none

non = None
print(type(non))


#set 

setdata = {10,23,4,34,45,2}
print(setdata)

'''-immutable
   -change relative position - no order maintained
   -remove duplicate data'''


#map
# dict

player = {7:'rohit',18:'virat',45:'rohit'}
print(player)

'''-mutable
    - change - update '''


# byte dta type ----------------------

hisdata = [10,20,40,30]
hisdata = bytes(hisdata)
hisdata = bytearray(hisdata)
print(hisdata)
for i in hisdata:
    print(i)

# range should be within(0,255) - bytes cannot be changed - immutable
    
# use bytearray to change elements - mutable







