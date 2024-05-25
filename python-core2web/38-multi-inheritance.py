#-------------------------------------------------------multiplle inheritance
'''
class parent1:

    def __init__(self):
        print("in constructor : parent1")

    def dispdata(self):
        print("in dispdata")

class parent2:

    def __init__(self):
        print("in constructor : parent2")

    def printdata(self):
        print("inn printdata")

class child(parent1,parent2):
    
    def __init__(self):
        print("in constructor: child")


obj =child()
obj.dispdata()
obj.printdata()


'''
#------------------------------------------------------ mro ( method resolution order )
'''
class parent1:

    def dispdata(self):
        print("in dispdata")

class parent2:

    def printdata(self):
        print("inn printdata")

class child(parent2,parent1):
    pass


obj =child()
obj.dispdata()
obj.printdata()
'''
#------------------------------------------------------'
'''
class parent1:

    def __init__(self):
        print("in constructor : parent1")

    def dispdata(self):
        print("in dispdata")

class parent2:

    def __init__(self):
        print("in constructor : parent2")

    def printdata(self):
        print("inn printdata")

class child(parent2,parent1):        #choose the init of left most parent
    pass

obj =child()
obj.dispdata()
obj.printdata()
'''

#=----------------------------------------------------------------------

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
    '''

#-----------------------------------------------------------------------
'''
class parent1:

    def __init__(self):
        print("in constructor : parent1")

    def dispdata(self):
        print("in dispdata")

class parent2:

    def __init__(self):
        print("in constructor : parent2")

    def printdata(self):
        print("inn printdata")

class child(parent2,parent1):

    def __init__(self):
        print("in constructor : child")

obj =child()
obj.dispdata()
obj.printdata()
'''
#-------------------------------------------------------
'''

class demo:

    def __init__(self):

        self.x=10
       

class demochild(demo):

    def __init__(self):
        self.y=20
        super().__init__()

    def printdata(self):
        print(self.x)
        print(self.y)

obj = demochild()
obj.printdata()
'''
#-------------------------------------------------------1.19

'''
class object:
    pass

class demo:

    def __init__(self):

        self.x=10
        super().__init__()
       

class demochild(demo):

    def __init__(self):
        self.y=20
        super().__init__()

    def printdata(self):
        print(self.x)
        print(self.y)

obj = demochild()
obj.printdata()

'''

#-----------------------------------------------------
'''
# class type:
#     def __init__(self):
#         print("hello")

#         return "bye"

class demo:

    def __init__(self):

        self.x=10
        super().__init__()
       

class demochild(demo):

    def __init__(self):
        self.y=20
        super().__init__()

    def printdata(self):
        print(self.x)
        print(self.y)

obj = demochild()
obj.printdata()

# print(type(obj))   
'''
#----------------------------------------------------------------