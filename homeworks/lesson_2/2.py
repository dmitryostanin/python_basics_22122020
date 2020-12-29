items_list = []
while True:
    item = input('Enter item (or nothing to quit): ')
    if item != '':
        items_list.append(item)
    else:
        break

print('List before: ', items_list)

swaps_number = len(items_list) // 2
swap = 1
index = 1
while swap <= swaps_number:
    temp = items_list[index]
    items_list[index] = items_list[index - 1]
    items_list[index - 1] = temp
    index += 2
    swap += 1

print('List after: ', items_list)
