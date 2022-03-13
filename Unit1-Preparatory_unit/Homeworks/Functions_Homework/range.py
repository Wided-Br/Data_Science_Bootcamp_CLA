def is_in_range(n, min, max):
    if (min <= n <= max):
        return True
    else:
        return False

num = int(input("Please enter a number: "))
inf = int(input("Enter the inferior born of the range: "))
sup = int(input("Enter the superior born of the range: "))
print(is_in_range(num,inf,sup))