from program2 import icc
class bcci(icc):
    def __init__(self):
        print("in constructor bcci")

class ipl(bcci):
    def __init__(self):
        print("in constructor ipl")

# obj = ipl()
obj = bcci()