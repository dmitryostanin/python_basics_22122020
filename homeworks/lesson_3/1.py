def divide(number_1: float, number_2: float):
    try:
        return number_1 / number_2
    except ZeroDivisionError as zde:
        print(f'Error: {zde}')
        return None


try:
    num_1 = float(input('Enter number #1: '))
    num_2 = float(input('Enter number #2: '))
    print(f'{num_1} / {num_2} = {divide(num_1, num_2)}')
except ValueError as ve:
    print(f'Wrong data!!! Error: {ve}')