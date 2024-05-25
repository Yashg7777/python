# def frequency(number):
#     frequency= {}
#     for num in number:
#         if num in frequency:
#             frequency[num] += 1
#         else:
#             frequency[num] = 1
#     return frequency

# number = [1,2,3,4,3,5,2,6,5,2,1,7,8,8,7,6,5,4,4,3,2,2,3,4,5,4,3,2]
# numbs = frequency(number)
# print(numbs)

# for key,value in numbs.items():
#     print(key,value)


def frequency(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num]= 1
    return frequency

numbers = [1,2,3,4,5,6,7,6,5,4,3,2,1,2,3,4,5,6,7,5,4,3,1,3,1,1,1,5,5,7,7,7,6,6,6,5,5,5,5,5,5,5,]
frequency_count = frequency(numbers)
for key,value in frequency_count.items():
    print(key,value)
 


#-------------------------------------------------------

'''
def frequency(number):
    max_num = max(number)  # Find the maximum number in the list
    frequency = [0] * (max_num + 1)  # Create a list to store frequencies, initialized with zeros
    for num in number:
        frequency[num] += 1  # Increment the frequency of the corresponding index
    return frequency

number = [1,2,3,4,3,5,2,6,5,2,1,7,8,8,7,6,5,4,4,3,2,2,3,4,5,4,3,2]
numbs = frequency(number)
print(numbs)
'''
#-------------------
