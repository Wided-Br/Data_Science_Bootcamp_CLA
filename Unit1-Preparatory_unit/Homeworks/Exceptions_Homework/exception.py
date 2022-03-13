a = 12
s = "hello"
try:
    print(a+s)
except TypeError:
    print(str(a) + s)
