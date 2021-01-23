class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_calc(self, thickness):
        weight_per_m2 = 25
        return self._length * self._width * weight_per_m2 * thickness


rd = Road(5000, 20)
print(f'Weight for the road {rd._length}m x {rd._width}m is {rd.weight_calc(5)}kg')
