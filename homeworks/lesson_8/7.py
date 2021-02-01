class Complex:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}+i{self.y}'

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Complex(self.x * other.x, self.y * other.y)


c1 = Complex(2, 3)
print(c1)
c2 = Complex(4, 5)
print(c2)
c1 = c1 + c2
print(c1)
c1 = c1 * c2
print(c1)
