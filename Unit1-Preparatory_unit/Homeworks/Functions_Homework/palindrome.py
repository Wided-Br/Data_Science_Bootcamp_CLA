import string

def is_palindrome(str):
    str=str.lower()                         #make the string all written in lowercase
    full_str=str.replace(" ","")            #remove the white spaces
    reversed_str = full_str[::-1]   
    return (full_str==reversed_str)


s = input("Please enter the string to check: ")
print(is_palindrome(s))