
#----------- METHOD RESOLUTION ORDER-------- # 

# 1) mro goes with dfs depth first search algorithm 

'''

class parent1:
    def __init__(self):
        print("in constructor parent 1")
    
    def dispdata(self):
        print("in disp data")

class parent2:
    def printdata(self):
        print("in printdata")

class child(parent2,parent1):
    pass

obj = child()
obj.dispdata()
obj.printdata()'''

#----------------------------------------
'''
class parent1:
    def __init__(self):
        print("in constructor parent 1")
    
    def dispdata(self):
        print("in disp data")

class parent2:
    def printdata(self):
        print("in printdata")

class child(parent2,parent1):
    pass

obj = child()
obj.dispdata()
obj.printdata()

print(child.mro())
'''
#-----------------------------------------
'''
class a:

    def fun(self):
        print("in fun: a")

class b:

    def fun(self):
        print("in fun: b")

class c:

    def fun(self):
        print("in fun: c")

class d(a,b):
    def fun(self):
        print("in fun: d")

        super().fun()

class e(b,c):
    def fun(self):
        print("in fun: e")
        super().fun()

class f(d,e):
    def fun(self):
        print("in fun: f")
        super().fun()

obj = f()

obj.fun()

print(f.mro())


'''
#diagram for this code 

# a   b   c
#   d   e
#     e

# output =   f, d, a, e, b, c 
#--------------------------------------------------------------------------------------------------


    # LECTURE 5 -- INHERITANCE  


#--------------------------------------------------------------------------------------------------

# dfs  dlr c3 linear=

'''
class parent1:

    def method(self):
        print("method: parent1")

class parent2:

    def method(self):
        print("method: parent2")

class child(parent1,parent2):
    pass

obj = child()
obj.method()
'''

#------------------------------
'''
class data:
    pass

class demo(data):
    pass

#method to print the name of parent of any class 

print(demo.__base__)
print(data.__base__)

print(dir(object))
print(dir(type))
'''
#-----------------------------
'''
class data:
    pass

print(dir(object))
print(dir(data))
'''
#----------------------------
'''
class demo:
    pass

obj1 = demo()
obj2 = demo()

print(id(obj1))
print(id(obj2))

print(obj1==obj2)
'''
#----------------------------------
'''
class demo:

    pass

obj1 = demo()
print(type(demo))
print(type(obj1))
'''
#----------------------------------
'''
class manager:

    def project(self):
        print("in projext manager")

class teamlead1(manager):
    pass

class teamlead2(manager):

    def project(self):
        print("in project teamlead2")
    
class developer(teamlead1,teamlead2):
    pass

obj=developer()
obj.project()
'''
#-----------------------------------------
'''
class boss:
    def report(self):
        print("boss : report")
        
class manager1(boss):
    def report(self):
        print("manager1 : report1")

class manager2(boss):
    def report(self):
        print("manager2 : report2")

class manager3(boss):
    def report(self):
        print("manager3 : report3")
      
class teamlead1(manager1,manager3):
    def report(self):
        print("teamlwad1:report")

class teamlead2(manager2,manager3):
    def report(self):
        print("teamlwad2:report")

class developer(teamlead1,teamlead2):
    def report(self):
        print("developer:report")

print(developer.__mro__)
print(developer.mro())'''

'''
           B
         
    M1    M2    M3

T1(M1,M3)  T2(M2,M3)  

      D1(T1,T2)

DIAGRAM FOR THIS CODE = d1,t1,m1,t2,m2,m3,b

'''
#------------------------------------


class boss:

    def report(self):
        print("mich ahe boss ")

class manager(boss):
    
    def report(self):
        print("manager: report to boss ")
   
class manager1(boss):

    def report(self):
        print("manager1: report to boss ")

class teamlead(manager,manager1):
        
        def report(self):
            print("teamlead : report to boss and manager ")
    
class developer(teamlead):

    def report(self):
        print("dev: report to teamlead")

print(developer.__mro__)



# here child class have 2 parent and 1 indirect parent - but  consider 2 parents only. --- multiple inheritance

class parent1:
    def fun(self):
        print("in fun parent1")

class parent2:
    def fun(self):
        print("in fun parent2")

class child(parent1,parent2):
    
    def fun(self):
        print("in fun child")


obj= child()
obj.fun()



#--------------------

class ajoba:
    def fun(self):
        print("in fun ajoba")


class parent1(ajoba):
    def fun(self):
        print("in fun parent1")

class parent2(ajoba):
    def fun(self):
        print("in fun parent2")

class child(parent1,parent2):
    
    def fun(self):
        print("in fun child")


obj= child()
obj.fun()


#---------------------



class boss:

    def report(self):
        print("mich ahe boss ")

class manager(boss):
    
    def report(self):
        print("manager: report to boss ")


class teamlead(manager,boss):
        
        def report(self):
            print("teamlead : report to boss and manager ")
    
class developer(teamlead):

    def report(self):
        print("dev: report to teamlead")

print(developer.__mro__)


#------------------------------------------------

'''


class boss:

    def report(self):
        print("mich ahe boss ")

class manager(boss):
    
    def report(self):
        print("manager: report to boss ")

class teamlead(boss,manager):                                                           #getting error
        
        def report(self):
            print("teamlead : report to boss and manager ")
    
class developer(teamlead):

    def report(self):
        print("dev: report to teamlead")

print(developer.__mro__)
'''

