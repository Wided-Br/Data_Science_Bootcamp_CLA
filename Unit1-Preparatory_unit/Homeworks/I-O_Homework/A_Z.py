import string

alphabet= string.ascii_uppercase
for letter in alphabet:
    with open(letter+".txt",'w') as file:
        file.write("This is file "+ letter)

print("**All files have been created successfully.**")