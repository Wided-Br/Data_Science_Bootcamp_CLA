import string

def reverse(str):
    reversed_str = str[::-1]
    return reversed_str

s = input("Enter the string to reverse: ")
print(reverse(s))