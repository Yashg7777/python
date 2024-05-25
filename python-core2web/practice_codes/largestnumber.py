def large_num(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

numbers = []
num_elements = int(input("enter a number : "))

for i in range(num_elements):
    number = int(input("enter num:"))
    numbers.append(number)
print(numbers)

large = large_num(numbers)
print(large)



#=----------------------------------


def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Test the function
nums = [10, 5, 8, 20, 3]
largest_num = find_largest(nums)
print(f"The largest number is {largest_num}")


def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

numbers=[]
numbers_element = int(input("enter a number :"))
for number in range(numbers_element):
    number=int(input())
    numbers.append(number)
print(numbers)

large = find_largest(numbers)
print(large)



def largenumber(numbers):
    largest = numbers[0]
    for number in numbers:
        if number >largest:
            largest = number
    return largest


numbers=[]

numberElements = int(input("enter number :"))
for number in range(numberElements):
    number=int(input())
    numbers.append(number)
print(numbers)

largeer = largenumber(numbers)
print(largeer)