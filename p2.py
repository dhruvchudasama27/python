# Write a program that takes a string as input and determines whether it is a palindrome (reads the same backward as forward). Ignore spaces and consider uppercase and lowercase letters as equal.

words = input("Enter any string :- ")
no_space = ''.join(words.split()).lower()
rev = "".join(reversed(no_space))

if no_space == rev:
    print("This string is palindrome")
else:
    print("This is not palindrome")

