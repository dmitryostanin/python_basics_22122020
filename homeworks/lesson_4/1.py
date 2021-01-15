from sys import argv


def salary(emp_ph, emp_r, emp_b):
    return emp_ph * emp_r + emp_b


try:
    _, production_hours, rate, bonus = argv
    production_hours = float(production_hours)
    rate = float(rate)
    bonus = float(bonus)
    print(f'Employee salary = {salary(production_hours, rate, bonus)}')
except ValueError as ve:
    print(f'Wrong data!!! Error: {ve}')