from itertools import count, cycle


# iterator 1
def iterator_1(start):
    for el in count(start):
        if el > 10:
            break
        else:
            print(f'{el} ', end='')


# iterator 2
def iterator_2(stop):
    counter = 0
    c_list = ['X', 'Y', 'Z']
    for el in cycle(c_list):
        if counter == stop:
            break
        print(f'{el} ', end='')
        counter += 1


iterator_1(3)
print()
iterator_2(10)
