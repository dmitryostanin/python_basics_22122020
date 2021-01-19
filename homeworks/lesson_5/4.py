digits = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
try:
    with open("task_4_1.txt", "r", encoding='UTF-8') as r_file:
        with open("task_4_2.txt", "w", encoding='UTF-8') as w_file:
            for line in r_file:
                sp_line = line.split(' - ')
                w_file.write(f'{digits[sp_line[0]]} - {sp_line[1]}')
                # print(f'{digits[sp_line[0]]} - {sp_line[1]}', end='')
except IOError as ioe:
    print(f'I/O error: {ioe}')
