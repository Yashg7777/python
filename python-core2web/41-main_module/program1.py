# code 1 - using from to get depencences
'''
from program2 import icc
class bcci(icc):
    def __init__(self):
        print("in constructor bcci")

class ipl(bcci):
    def __init__(self):
        print("in constructor ipl")

# obj = ipl()
# obj = bcci()
        
# print(ipl.mro())


if __name__ == '__main__':
    ipl()
else:
    bcci()
'''

# code 2
    

# from program2 import icc
class bcci():
    def __init__(self):
        print("in constructor bcci")

class ipl(bcci):
    def __init__(self):
        print("in constructor ipl")

# obj = ipl()
# obj = bcci()
        
# print(ipl.mro())


if __name__ == '__main__':
    ipl()
else:
    bcci()
