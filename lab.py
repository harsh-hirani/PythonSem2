# p4 6 - WAP to check whether an input sentence is a pangram or not. 
import string
alphabets = list(string.ascii_lowercase)
used_alphabets = set()
str = input('Enter a sting to check if it is pangram or not: ')

for char in str.lower():
    if char in alphabets:
        used_alphabets.add(char)
if len(used_alphabets) == 26:
    print("yes")
else:
    print('no')