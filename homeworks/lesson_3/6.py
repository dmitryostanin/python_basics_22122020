def int_func(word: str):
    return word.capitalize()


try:
    text = input('Enter text: ')
    text_list = text.split(sep=' ')
    for index in range(0, len(text_list)):
        text_list[index] = int_func(text_list[index])
    print(f"Modified text: {' '.join(text_list)}")
except ValueError as ve:
    print(f'Wrong data!!! Error: {ve}')
