while True:
    month = int(input('Enter month (1-12): '))
    if month < 1 or month > 12:
        print('Wrong data!!!')
    else:
        break

month_list = ['Winter',
              'Winter',
              'Spring',
              'Spring',
              'Spring',
              'Summer',
              'Summer',
              'Summer',
              'Autumn',
              'Autumn',
              'Autumn',
              'Winter']
month_dict = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer',
              7: 'Summer', 8: 'Summer', 9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'}

print(f'Month number {month} is {month_list[month - 1]}')
print(f'Month number {month} is {month_dict.get(month)}')
