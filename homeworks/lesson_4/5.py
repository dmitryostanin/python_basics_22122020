from functools import reduce
print(reduce(lambda x, y: x * y, [num for num in range(100, 1001, 2)]))
