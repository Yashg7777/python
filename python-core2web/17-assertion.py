name = input("Enter your name :")
age = int(input("enter your age :"))

assert age>0,"....age -ve is not allowed."

if(age>18):
    print("u r eligible for voting")

else:
    print(name,"not eligible.")
    


def divide(x,y):
    assert y!=0,"divisor cannot be zero"
    print(x/y)

divide(10,0)

# calculate area of circle

def area(radius):
    assert radius >= 0
    return 3.14* radius**2

result=area(-5)

#factorial

 