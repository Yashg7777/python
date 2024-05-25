def prime(number):
    if number <2:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

number = 17
primes = prime(number)
print(primes)

def prime(number):
    if number < 2:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False
        return True
    
number = int(input("enter a number :"))
prime_number=prime(number)
print(prime_number)