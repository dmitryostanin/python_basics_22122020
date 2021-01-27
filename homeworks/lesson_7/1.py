class Matrix:
    def __init__(self, elements):
        self.elements = elements

    def __str__(self):
        result = 'Matrix:\n'
        for i in self.elements:
            for j in i:
                result += str(j) + ' '
            result += '\n'
        return result

    def __add__(self, other):
        result = []
        for i in range(0, len(self.elements)):
            temp = []
            for j in range(0, len(self.elements[i])):
                temp.append(self.elements[i][j] + other.elements[i][j])
            result.append(temp)
        return Matrix(result)


m1 = Matrix([[9, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[1, 8, 7], [6, 5, 4], [3, 2, 1]])
print(m1)
print(m2)
print(m1 + m2)
