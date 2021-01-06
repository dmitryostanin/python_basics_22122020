def my_func(x: int, y: int) -> float:
    x_pow = 1
    for item in range(1, abs(y) + 1):
        x_pow *= x
    return 1 / x_pow


try:
    num_1 = int(input('Enter int X: '))
    num_2 = int(input('Enter int Y (Y < 0): '))
    if num_2 >= 0:
        raise ValueError('Y must be negative!')
    else:
        print(f'{num_1} ^ {num_2} = {my_func(num_1, num_2)}')
except ValueError as ve:
    print(f'Wrong data!!! Error: {ve}')
