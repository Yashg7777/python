def is_palindrome(string):
    reverse_string = string[::-1]
    return string == reverse_string

word = input("enter input word : ")

if is_palindrome(word):
    print(word, "is palindrome")
else:
    print("not palindrome")

#---------------------------------------

def palindrome(word):
    reverse_word = word[::-1]
    return word == reverse_word

word = input("enter a word to check : ")

if palindrome(word):
    print(word)
else:
    print("nothing")

#---------------------------------------


word = input("enter a word to check : ")
if word == word[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")

#---------------------------------------

def palindrome(word):
    if word == word[::-1]:
        print("The word is a palindrome.")
    else:
        print("The word is not a palindrome.")

word = input("enter a word to check : ")

pal = palindrome(word)

#------------------------------