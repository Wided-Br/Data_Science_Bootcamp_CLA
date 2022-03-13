# Read all of the content of the file in one variable.
file = open("student_names.txt")
students = file.read()
print('The initial students names are:')
print(students)
print("\n")

# Write a list of random names to your file.
new_students = """
Michael Scott
Jim Halpert
Pam Beesly
Dwight Schrute
Kevin Malone"""
students = students + new_students
file = open("student_names.txt","w")
file.write(students)
file.close
print("**A list of new students names is added successfully to the file.**\n\n")

# Read the first n lines of the file.
file = open("student_names.txt")
nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
line_count = len(nonempty_lines)
file.close()
print("Note that There are ", line_count, " lines in the file.")
n = int(input("Please enter the number of lines that you want to read from the beginning: "))
file = open("student_names.txt")
for i in range(n):
    line = file.readline()
    print(line, end = '')
file.close()
print("\n\n")

# Read the last n lines of the file.
file = open("student_names.txt")
print("Note that There are ", line_count, " lines in the file.")
m = int(input("Please enter the number of lines that you want to read from the end: "))
for line in (file.readlines() [-m:] ):
    print(line, end = '')
file.close()

# Check if the name x is in the file.
file = open("student_names.txt")
students = file.read()
search_name = input("\n\nPlease enter the name that you want to search: ")
if (search_name in students):
    print("The name exists.")
else:
    print("The name doesn't exist.")
file.close()