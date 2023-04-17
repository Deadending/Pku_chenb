'''
@Func: Count the number of English letters, spaces, numbers and other characters in a string
@Author：jlzhong0709@gmail.com
@Date:12/04/2023
'''
import string


s = input("input a string:")
letter = 0
space = 0
digit = 0
other = 0
for c in s:
    if c.isalpha():
        letter += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        other += 1
print("There are %d letters, %d spaces, %d digits and %d others characters in your string." %(letter,space,digit,other))