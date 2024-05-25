from program1 import *
#code 1 = getting called by main module 

'''class icc:
    def __init__(self):
        print("in constructor icc")'''



# code 2  with code 1 of p1
        
'''from program1 import *

class icc:
    def __init__(self):
        print("in constructor icc")

if __name__ == '__main__':
    print("in module 2 ")'''

# code 3 with code 2 of p1
    
# from program1 import *
'''
class icc:
    def __init__(self):
        print("in constructor icc")

if __name__ == '__main__':
    print("in module 2 ")
else:
    ipl()'''


#code 4 with code 2 of p1

class icc:
    def __init__(self):
        print("in constructor icc")

if __name__ != '__main__':
    print("in module 2 ")
else:
    ipl()