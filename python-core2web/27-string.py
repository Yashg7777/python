#===============================string======================================#
"""
str='helo'
print(str)
print(type(str))            #class str
print(len(str))

str1="helo"
print(str1)

str2='''helo
good
morning'''
print(str2)

str3="welcome \t to \n kopargaon"
print(str3)

str4=r"welcome \t to \n kopargaon"            #<raw string
print(str4)

str5="\u0906 \u0908"
print(str5)

str6="\u0915 \u0916"

#access
#1.slicing 2.index

str7="spiderman"
print(str7[3])
print(str7[4])
print(str7[-3])


print(str7 [::3])
print(str7[2:5:])
print(str7[-3::-1])


str8 = "core2web"
str9 = "core2web"

print(str8==str9)

str10 ="incubator"
str11 ="Incubator"

print(str10==str11)

print(str10<str11)
"""

#methods in string

'''
1.capitalize   <- first letter capital
2.index
3.isalphanuric
4.isascii
5.isalpha
6.isdecimal
7.rstrip
8.lstrip
9.strip
10.
11.
12.
13.
14.
15.
16.
17.
18.
19.
20.
21.
22.
23.
24.
25.
26.
27.
28.
29.
30.
31.
32.
33.
34.
35.
36.
37.
38.
39.
40.
41.
42.
43.
44.

'''

str1 = "Core2web\tIncubator"
str2 = "core2web Incubator"

print(str1.capitalize())    #Core2web incubator

print(str1.casefold()==str2.casefold())

print(str1.count('b'))

print(str1.endswith('tor'))

print(str1.expandtabs(4))

print(str1.find('web'))


fruit='grapes'
character='a'

print(fruit.find(character))

#--------------------------------

string1 = input("enter main string")
sub=input("enter sub string")

# if sub in string1:
#     print(sub+' found')
# else:
#     print(sub +" not found")


n= string1.find(sub)
if n == -1:
    print(sub + "not found")
else:
    print(sub + "found{}".format(n))

#------------------------------------
string1 = input("enter main string")
sub=input("enter sub string")

# if sub in string1:
#     print(sub+' found')
# else:
#     print(sub +" not found")


n= string1.rfind(sub)
if n == -1:
    print(sub + "not found")
else:
    print(sub + "found{}".format(n))
#-----------------------------------

str1 = "core2web"

print(str1.isalnum())
print(str1.isdigit())
print(str1.isdecimal())
print(str1.isascii())
print(str1.isalpha())

#-----------------------------------

str1 = ["core2web","incubator","biencaps"]
str2 = "core2webs"

print("-".join(str1))
print("-".join(str2))

#-----------------------------------

str2 = "core2webs"

print(str2.rjust(12,"#"))
print(str2.ljust(12,"#"))

#-----------------------------------

str1 ="    core2web     "

print(str1)

print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())

#-------------------------------

str1 = "core2webincubator"          #<- return as tuple 
print(str1)

print(str1.partition("web"))
print(str1.rpartition("hash"))
print(str1.partition("hash"))

#--------------------------------

str1 = "core2we,bincubator biencaps"

print(str1.split(","))

#--------------------------------------

stra=int(input("a="))
strb=int(input("b="))
strc=int(input("c="))

x,y,z=[int(val) for val in input("Enter first int :").split(" ")]
print(x+y+z)

print(stra+strb+strc)

#_-------------------------------------
