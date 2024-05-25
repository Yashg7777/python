def factorial_number(n):
    if n == 0:
        return 1
    else:
        return n * factorial_number(n-1)


number = int(input("enter a number : "))
result = factorial_number(number)
print(result)


def factorial(n):
    if n ==0 :
        return 1
    else:
        return n * factorial(n-1)

number = 4
result = factorial(number)
print(result)




a = 10
b = 20
c=5

a,b,c=None,None,None

a=input("")
b=input("")
c=input("")
# c=++a
list=[a,b,c]
print(list)

