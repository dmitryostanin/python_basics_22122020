subjects_dict = {}
try:
    with open("task_6.txt", "r", encoding='UTF-8') as file:
        for line in file:
            sp_line = line.split(' ')
            h_sum = 0
            for index in range(1, 4):
                if sp_line[index] != '-':
                    h_sum += float(sp_line[index].split('(')[0])
            subjects_dict.update({sp_line[0].split(':')[0]: h_sum})
    print(subjects_dict)
except IOError as ioe:
    print(f'I/O error: {ioe}')
