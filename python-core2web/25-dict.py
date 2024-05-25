#========================================================
#  ******************DICTIONARY*******************      =
#======================================================== 
'''
player1 = {45:'rohit',77:'shubhman',18:'virat',1:'kl'}
print(player1)
print(type(player1))
'''

'''

myinfo={'name':'yash',3:['core2web','biencaps','incubator']}
print(myinfo)
'''

#nested
'''
player1 = {45:'rohit',77:'shubhman',18:'virat',1:'kl','next to bat':{96:'shreyash',63:'sky',8:'jaddu'}}
print(player1)
print(type(player1))
'''
#access
'''
print(player1[18])
print(player1[45])
print(player1['next to bat'])
print(player1['next to bat'][63])
'''
# replace in dict 
'''
player1 = {45:'rohit',77:'shubhman',18:'virat',1:'kl','next to bat':{96:'shreyash',63:'sky',8:'jaddu'},77:'xyz'}
print(player1)
'''
#update
'''
player1[100]='virat kohli'

print(player1)

'''
#methods------------------

'''
access element from dictionary
1.get
2.items
3.keys
4.values

5.popitem
6.clear
7.pop

8.copy
9.update
10.setdefaulf
11.fromkeys

'''




'''
player2={45:'rohit',77:'shubhman',18:'virat',1:'kl'}

print(player2)

print(player2.get(18))
player2={45:'rohit',77:'shubhman',18:'virat',1:'kl'}
print(player2.items())
for key, value in player2.items():
    print(key,':',value)

print(player2.keys())

print(player2.values())



player2.popitem()
print(player2)

player2.pop(18)
print(player2)
'''
# player2.clear()
# print(player2)


player2={45:'rohit',77:'shubhman',18:'virat',1:'kl'}
'''
newdata={63:'surya',33:'hardik'}

player2.update(newdata)
print(player2)

player2.setdefault(18,'kohli')'''  # if key present, do nothing else add it.


val= player2.setdefault(18,'kohli')
print(player2)
print(val)

val= player2.setdefault(19,'kohli')
print(player2)
print(val)


