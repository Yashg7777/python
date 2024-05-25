from program4 import *

class core2web():
    def __init__(self):
        print("in core2web constructor")

class incubators(core2web):
    def __init__(self):
        print("in incubators constructor")
        super().__init__()

if __name__ == '__main__':
    incubators()
else:
    biencaps()