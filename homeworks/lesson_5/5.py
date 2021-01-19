import random
try:
    with open("task_5.txt", "w", encoding='UTF-8') as w_file:
        for number in range(random.randint(1, 10)):
            w_file.write(f'{random.randint(0, 100)} ')
except IOError as ioe:
    print(f'I/O error: {ioe}')
try:
    with open("task_5.txt", "r", encoding='UTF-8') as r_file:
        for line in r_file:
            sp_line = line.split(' ')
        n_sum = 0
        print(f'Numbers: ', end='')
        for index in range(len(sp_line) - 1):
            n_sum += int(sp_line[index])
            print(f'{sp_line[index]} ', end='')
        print(f'\nSUM = {n_sum}')
except IOError as ioe:
    print(f'I/O error: {ioe}')
