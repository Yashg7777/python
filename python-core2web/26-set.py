#array-similar-continues-typecode(restriction)-indexing-reverseing-
#list-dynamic-dissimilar-duplicate-index-negative-mutable
#tuple-non changeable-immutable-dissimilar
#dict- 2-obj - keyvalue pair -key unique -value..duplicated

#set- no duplication

'''
set0={1,2,3,4,5}
print(set0)
print(type(set0))

set1={1,"a",10.5,0,True,False}
print(set1)

set2={'ashish','kanha','badhe','rahul'}
print(set2)

set3=set([10,20,30,40])
print(set3)

set4=set(10,20,30,40)
print(set4)

set5=set(10)
print(set5)
'''
#access set
'''
setdata ={1,2,3,4,5}

#     print(setdata[2])  #<- set object is not subscribtable

#     setdata[2]=50     #<- object does not support item assignment

setdata.add(6)
print(setdata)

setdata1 =frozenset([1,2,3,4,5])
print(setdata1)
'''

#methods in set
'''
1.add
2.copy
3.difference
4.difference_update
5.discard
6.intersection
7.intersection_update
8.isdisjoint
9.issubset
10.issuperset
11.symmetric_difference
12.symmetric_difference_update
13.union
14.update
15.pop
16.remove
17.clear

'''

#methods

sets={1,2,3,4}
sets1={3,4,5,6}

sets.add(10)
print(sets)

sets1=sets.copy()
print(sets1)

#sets2=sets.difference(sets1)
#print(sets2)

# sets.difference_update(sets1)
# print(sets)

#sets.discard(3)
#print(sets)

# sets2=sets.intersection(sets1)
# print(sets2)


# sets.intersection_update(sets1)
# print(sets)

# print(sets.isdisjoint(sets1))

# print(sets.issubset(sets1))

# print(sets.issuperset(sets1))

# sets2=sets.symmetric_difference(sets1)
# print(sets2)

# sets2=sets.symmetric_difference_update(sets1)
# print(sets2)

# sets2=sets.union(sets1)
# print(sets2)

# sets.update(sets1)
# print(sets)

# sets.pop()
# print(sets)

# sets.clear()
# print(sets)

# sets.remove(20)
# print(sets)



