string = input('Enter string: ')
print('String as list:')
string_list = string.split(sep=' ')
for index, item in enumerate(string_list, start=1):
    print(f'{index} {item[:10]}')
