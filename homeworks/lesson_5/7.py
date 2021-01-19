import json
companies_list = [{}, {}]
try:
    with open("task_7.txt", "r", encoding='UTF-8') as file:
        p_count, p_sum = 0, 0
        for line in file:
            sp_line = line.split(' ')
            profit = float(sp_line[2]) - float(sp_line[3])
            if profit > 0:
                p_count += 1
                p_sum += profit
            companies_list[0].update({sp_line[0]: profit})
    if p_count > 0:
        avg_profit = p_sum / p_count
        print(f'Average profit of {p_count} firm(s) = {avg_profit}')
        companies_list[1].update({"average_profit": avg_profit})
    else:
        print('No profitable firms!')
    print(companies_list)
    with open("task_7.json", "w") as json_file:
        json.dump(companies_list, json_file)
except IOError as ioe:
    print(f'I/O error: {ioe}')
