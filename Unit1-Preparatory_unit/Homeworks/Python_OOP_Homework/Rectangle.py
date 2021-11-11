class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def calc_area(self):
        return (self.length * self.width)


m = int(input("Enter the rectangle's length: "))
n = int(input("Enter the rectangle's width: "))
ABCD = Rectangle(m,n)
print(ABCD.calc_area())
