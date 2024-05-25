#methods

'''

1)class method
2)instance method / object method
3)static method


'''
#instance method
class player:

    teamName="india"

    def __init__(self,jerNo,pName):
        print("In Constructor")
        self.jerNo= jerNo
        self.pName= pName

    def playerInfo(self):
        print(self.jerNo)
        print(self.pName)
        print(self.teamName)

cric1=player(18,"virat")
cric2=player(45,"rohit")

cric1.playerInfo()
cric2.playerInfo()

player.teamName="bharat"

cric1.playerInfo()
cric2.playerInfo()

# player.playerInfo() --- positional argument error - instance method get called only by object.


#class method----------------------------


class player:

    teamName="india"

    def __init__(self,jerNo,pName):
        print("In Constructor")
        self.jerNo= jerNo
        self.pName= pName

    @classmethod
    def playerInfo(cls):
        # print(self.jerNo)
        # print(self.pName)
        print(cls.teamName)

cric1=player(18,"virat")
cric2=player(45,"rohit")

player.playerInfo()
cric1.playerInfo()

#--------------------------------------------------------

#static method

#--------------------------------------------------------
class player:

    teamName="india"

    def __init__(self,jerNo,pName):
        print("In Constructor")
        self.jerNo= jerNo
        self.pName= pName

    @staticmethod
    def playerInfo():
        # print(self.jerNo)
        # print(self.pName)
        print(player.teamName)

cric1=player(18,"virat")
cric2=player(45,"rohit")

player.playerInfo()
cric1.playerInfo()

#------------------------------------------------


def outer():
    def inner():
        a=10
        b=20
        c=a+b
        return "hello,i'm inner function",c
        
    return inner
ans=outer()
m1=ans()
for i in m1:
    print(i)

#-------------------
    
def outer():
    print("i am outer")
    def inner():
        return "hello,i'm yash"
    return inner
outer()

#-----------------1
def outer():
   
    def inner():
        return "hello,i'm yash"
    return inner
ans=outer()
print(ans)
#-----------------2

def outer():
    def inner():
        return "helo,i'm yash"
    return inner
obj=outer()
retinner=obj()
print(retinner)

#-----------------3
