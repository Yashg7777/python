#write a program to find a maximum between two numbers 
'''
def max(x,y):
    if x<y:
        print(y," is greater number")
    elif x>y:
        print(x," is greater number")
    else:
        print("number are equal.")

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
max(a,b)
'''

#write a program to check wheather the number is negative,positive or equal to zero.
'''
def posneg(number):
    if number > 0:
        print("number is positive:",number)
    elif number < 0:
        print("number is negative:",number)
    else:
        print("number is equal to 0.")

a=int(input("Enter a number: "))
posneg(a)

'''

#write a program to find number is even or odd

'''
def evenodd(number):
    if number%2==0:
        print("Number is even :",number)
    else:
        print("Number is odd:",number)

a=int(input("Enter a number "))
evenodd(a)

'''
#write a program to find wheater the number is divisible by 5 or not.
'''
def div(number):
    if number%5==0:
        print("Number is divisible by 5 :",number)
    else:
        print("Number is not divisible by 5:",number)

no=int(input("enter a number:"))
div(no)

'''

#write a program to take integer range from 0 to 6 and print corresponding weekday

'''
def printday(integer):

    weekdays=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

    if 0 <= integer <= 6:
        print("the day in a week is :",weekdays[integer])
    else:
        print("the input is invalid.")

x=int(input("enter number between 0 to 6 :"))
printday(x)

'''
#write a program to check character is alphabet or not

'''
def char(character):
    if len(character)==1 and ('a' <= character <= 'z' or 'A'<=character<='Z'):
        print("{} is a character.".format(character))
    else:
        print("{} is not a character.".format(character))

a=input("enter a character :")
char(a)


'''
#wp to take number of month and print days in that month.
'''
def days_in_month(month):

    days={

        1:'january have 31 days.',
        2:'feb have 28 days.',
        3:'march have 31 days',
        4:'april have 30 days.',
        5:'may have 31 days.',
        6:'june have 30 days.',
        7:'july have 31 days.',
        8:'august have 31 days.',
        9:'september have 30 days.',
        10:'october have 31 days.',
        11:'november have 30 days.',
        12:'december have 31 days.',
    
    }

    if month in days:
        print( days[month])
    else:
        return -1
    

month=int(input("enter number of month:"))
days_in_month(month)
'''

#write a prgram to check given number is greater than 10 or not
'''

def check(number):
    if number >=10:
        print("no is greater than 10")
    else:
        print("no is not greatwer than 10")

x=int(input("enter a number:"))
check(x)

'''

#write a program to check input character is vowel or consonant


'''
def char(character):

    vowel=['a','e','i','o','u']
    if len(character)==1:
        if character in vowel:
            print("{} is a vowel".format(character))
        else:
            print("{} is consonant.".format(character))
    else:
        print("please enter only one character.")

character=input("enter a char:")
char(character)
'''


#write a program to check leap year or not

def leap(year):
    if year%4==0 and year%100!=0:
        print("leap year")
    else:
        print("non leap year")

year=float(input("enter year:"))
leap(year)