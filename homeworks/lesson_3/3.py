def my_func(arg_1: float, arg_2: float, arg_3: float) -> float:
    def min_in_3(num_1: float, num_2: float, num_3: float) -> float:
        n_min = num_1
        if num_2 < n_min:
            n_min = num_2
        if num_3 < n_min:
            n_min = num_3
        return n_min
    return arg_1 + arg_2 + arg_3 - min_in_3(arg_1, arg_2, arg_3)


number_1, number_2, number_3 = 9, 2, 3
try:
    print(f'Sum of two max numbers: {my_func(number_1, number_2, number_3)}')
except ValueError as ve:
    print(f'Wrong data!!! Error: {ve}')
