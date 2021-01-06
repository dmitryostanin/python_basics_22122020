def sum_numbers(string: str):
    not_ready_to_quit = True
    numbers_list = string.split(sep=' ')
    if 'Q' in numbers_list:
        q_index = numbers_list.index('Q')
        not_ready_to_quit = False
    else:
        q_index = len(numbers_list)
    try:
        list_sum = 0
        for index in range(0, q_index):
            list_sum += float(numbers_list[index])
    except Exception as te:
        print(f'Wrong data!!! Error: {te}')
        return None, not_ready_to_quit
    return list_sum, not_ready_to_quit


global_sum = 0
ok = True
while ok:
    numbers = input('Enter numbers separated by " " or/and "Q" to quit: ')
    temp_sum, ok = sum_numbers(numbers)
    if temp_sum is None:
        break
    else:
        global_sum += temp_sum
    print(f'Now sum is {global_sum}')
