try:
    with open("task_3.txt", "r", encoding='UTF-8') as file:
        count, s_sum, s_value = 0, 0, 20000
        print(f'Employees with salary below {s_value}:')
        for line in file:
            sp_line = line.split(' ')
            if float(sp_line[1]) < s_value:
                print(f'Employee: {sp_line[0]} Salary: {sp_line[1]}', end='')
            count += 1
            s_sum += float(sp_line[1])
        if count > 0:
            print(f'Avg salary: {s_sum / count}')
except IOError as ioe:
    print(f'I/O error: {ioe}')
