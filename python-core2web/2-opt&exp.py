# operators 


# print(x + y ) ---- operator overloading as it contain 2 class x ,y ;

# go to yelp()- type int see tye metyos defined yere   __add__(self, value. /)

# in pytyon everytying is class  we cannot add or do operation on class sucy lide tyis 
# so pytyon yas inbuild metyods for it all operators tyat perform operation in back




# types of operators 

# 1. unary    2.binary      3.ternary

# a + b     //a,b are operand and + is operator

# 1) single operator is and single operand is unary operator 

#pytyon does not support  ++ -- 

a = 10
b = 10
print(a+++b)
ans = -a;
print(ans)


#binary operator

'''  1. aritymatic =   + , - , /-float , * , % , //-floor division , **-power ,

     2. relational =  < , > , <= , >=, == , ! =   
     
     3. logical = and , or , not   
     
     4. assignment =     =,+=,-=,/=,%=,*=   
     
     5. bitwise =   & - bitwise and  , |- bitwise or ,  ^- bitwise xor , <<-left syift , >>- rigyt syift , ~ -negation/complement operator
     
     6. identity = is , is not 
     
     7. membersyip = in , not in '''


# 1.aritymatic 

x = 2
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x // y)
print(x ** y)

# 2.relational operator

g = 10
y = 20

print(g<y)
print(g>y)
print(g<=y)
print(g>=y)
print(g==y)
print(g!=y)

# 3.logical operator

# logical boolean operator
k = True                                        
'''consider as boolean and return boolean'''
y = False

print(k and y)
print(k or y)
print(not k)

# logical logical operator

o = 4                                         
'''give integer as return '''
p = 9

print(o and p)
print(o or p)
print(not p)

''' not always answer in boolean'''

# 4.assignment operator

l = 10
m = 3
print(l)

l /= m
print(l)

# 5. bitwise operator

''' & -bitwise and ,| - bitwise or ,^- bitwise xor ,>> ,<< ,~ - bitwise not '''

''' and     or      xor
   
   0 0 0   0 0 0   
   0 1 0   0 1 1 
   1 0 0   1 0 1 
   1 1 1   1 1 1  '''


s=10     #00001010
d=5      #00000101

print( s & d )
print( s | d )
print(s << 2)
print("d is :",d >> 3)
print(~s) 

# 6. identity operator

listd = [10,20,30]
j =10
d = 12
print(j not in d)
print(id(j))
print(id(d))
print( j is d)
print( j is not d)

# 7 .membership operator

print(j in listd)
print(d not in listd)

d =[1,12,13,15]
k=17
print(k not in d)
print(j in d)
print(j not in d)
print(j is d)
print(j is not d)

