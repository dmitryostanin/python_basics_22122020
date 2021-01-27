class Cell:
    def __init__(self, parts: int):
        self.parts = parts

    def __add__(self, other):
        return Cell(self.parts + other.parts)

    def __sub__(self, other):
        if self.parts > other.parts:
            return Cell(self.parts - other.parts)
        else:
            print('\nWrong operation, subtraction prohibited!')
            return self

    def __mul__(self, other):
        return Cell(self.parts * other.parts)

    def __truediv__(self, other):
        return Cell(self.parts // other.parts)

    def make_order(self, parts_per_row):
        result = ''
        for index in range(0, self.parts):
            result += '\n*' if (index) % parts_per_row == 0 else '*'
        return result


c1, c2, c3 = Cell(10), Cell(20), Cell(30)
print(c1.make_order(4))
c1 = c1 + c2
print(c1.make_order(10))
c1 = c1 * c2
print(c1.make_order(120))
c1 = c1 - c2
print(c1.make_order(120))
c1 = c1 / c3
print(c1.make_order(10))
c1 = c1 - c3
print(c1.make_order(5))
