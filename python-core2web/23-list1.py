#---------------------------LIST-------------------------------#

'''  

1. list is built in mutable sequence
2. if no argument is given ,the constructor creates a new empty list.
3.the argument must be an iterable if specified
4.it is changeable
5.list have total 11 methods
'''

#methodss in list

'''
3-insert method
3-delete method
5-data manipulation method



list --
 
multiple objects
growable
can add multiple type of datatypes
78*

'''

#------------------list creation methods---------------------------#

'''   
    1. list literals     batsman=['rohit','virat','shreyash']
    2. using constructor      
    3. comprenshion
        
'''


# -----------------------list literals---- any datatype can be used inn list. [{}],[()],[{:}],[]
'''
batsman = ['rohit','shubhman','virat','shreyash','kl']
print(batsman)
print(type(batsman))

batrun = ['rohit',47,'shubbhman',67,'virat',117]
print(batrun)
print(type(batrun))
print(type(batrun[0]))

employee = [{10,'ashish',1.5},{9,'kanha',1.67},{8,'rahul',2.0}]
print(employee[0])
print(type(employee))
print(type(employee[0]))


player=[{18:'virat'},{45:'rohit'}]
print(player)
print(type(player))
print(type(player[0]))

'''
# ---------------------------------------------list constructor----

""" 
0.convert every datatype to list.
1.only 1 argument can be passed.
"""
#--------------------
'''
player= list()
print(player)
print(type(player))
'''
#---------------------
'''
listdata=[10,20,30,40]

batsman = list(listdata)           #<-- constructor
print(batsman)
print(type(batsman))
'''

# ------------------------------------------list comprehension


""" 1.no predefind help 
    2.no third party data type
    3.operationable
"""
'''
normlist = [num for num in range(1,11)]

normlist = [num*num for num in range(1,11)]
print(normlist)
print(type(normlist))

even_list = [num*num for num in range(1,11) if num % 2 ==0]
print(even_list)
print(type(even_list))

odd_list = [num*num for num in range(1,11) if num %2 == 1]
print(odd_list)
print(type(odd_list))

'''

# accessing elements from list
#1.index
#2.slicing

'''
#indexing
player = ['rohit','virat','shubhman','shreyash']

print(player[0])
print(player[3])
print(player[1])


     #       0       1          2       3
player = ['rohit','virat','shubhman','shreyash']
  #         -4      -3      -2          -1


print(player[-2])
print(player[-3])
print(player[-1])
'''

#slicing
'''
player = ['rohit','virat','shubhman','shreyash']

print(player[2::])
print(player[1:4:2])
print(player[:5:2])

print(player[::3])
'''

#method from list class ---------------------------------------


#access methods 

'''1.append
   2.extend
   3.index-insert
'''
'''
player =['rohit','shubman','virat','shreyash','kl']

print(player)

player.append('sky')
print(player)

player.extend(['jaddu','bumrah','shami'])
print(player)

player.insert(3,'hardik')
'''


#delete from list

'''1.remove
   2.pop
   3.clear
'''
'''
player.remove('sky')   #<---index cannot be given for remove
print(player)

player.pop()    #<- will del last element or provide index number
print(player)

player.clear()
print(player)
'''


# methods  delete
'''

1.count
2.index
3.sort
4.reverse
5.copy

'''
'''
player =['rohit','shubman','virat','shreyash','kl']
print(player.count('rohit'))

print(player.index('rohit'))

player.reverse()
print(player)

print(player.count('rohit'))

player.sort()
print(player)

batsman = player.copy()
print(batsman)
'''


#-------------------------------- Nested List ------------------------------------#

'''
lang = ['cpp','java','python',['go','rust','dart']]
print(lang[1])
print(lang[3])   #print whle list from go ...dart
print(lang[3][1])  #print only first element in nested list 

'''
#----------------------------------------------------------------------------------

#copy --- shallow copy --- deep copy

'''


#python store data at address level internally

lang = ['cpp','java','python']
newlist =lang.copy()

print(lang)
print(newlist)

print(id(lang)==id(newlist))
lang[1]='js'

print(lang)
print(newlist)

'''


'''

lang = ['cpp','java','python',['go','rust','dart']]
newlist=lang.copy()

print(lang)
print(newlist)

print(id(lang)==id(newlist))

lang[3][1]='js'

print(lang)
print(newlist)

'''

import copy as cp

lang = ['cpp','java','python',['go','rust','dart']]
newlist=cp.deepcopy(lang)

print(lang)
print(newlist)

print(id(lang)==id(newlist))

lang[3][1]='javaScript'

print(lang)
print(newlist)

