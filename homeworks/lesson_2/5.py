my_list = [7, 6, 3, 3, 2]
number = int(input('Enter new number: '))
print(f'List before: {my_list}')
my_list.append(number)
my_list.sort(reverse=True)
print(f'List after: {my_list}')
