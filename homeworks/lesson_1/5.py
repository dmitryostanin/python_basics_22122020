earnings = float(input('Enter earnings: '))
costs = float(input('Enter costs: '))
profit = earnings - costs
if profit > 0:
    print('Company is profitable!')
    print(f'Revenue profitability is {profit / earnings}')
    employee_number = int(input('Enter employee number: '))
    print(f'Profit per employee is {profit / employee_number}')
else:
    print('Company is unprofitable!')
