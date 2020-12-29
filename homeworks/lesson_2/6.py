count = 0
goods = []
while True:
    answer = input('Do you want to enter new item? (Y/N): ')
    if answer.upper() == 'N':
        break
    elif answer.upper() == 'Y':
        count += 1
        name = input("Enter good's name: ")
        price = input("Enter good's price: ")
        amount = input("Enter good's amount: ")
        unit = input("Enter good's unit: ")
        goods.append((count, {"name": name, "price": price, "amount": amount, "unit": unit}))
    else:
        continue

names, prices, amounts, units = [], [], [], []
analytics = {}
for item in goods:
    names.append(item[1]["name"])
    prices.append(item[1]["price"])
    amounts.append(item[1]["amount"])
    units.append(item[1]["unit"])
analytics.update({"names": names})
analytics.update({"prices": prices})
analytics.update({"amounts": amounts})
analytics.update({"units": units})

print('Analytics: ')
print(analytics)
