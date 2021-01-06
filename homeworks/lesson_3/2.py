def print_person_data(name, surname, b_year, city, email, phone):
    print(f'{name} {surname}, {b_year}, {city}, {email}, {phone}')


p_name = input('Enter name: ')
p_surname = input('Enter surname: ')
p_b_year = input('Enter year of birth: ')
p_city = input('Enter city: ')
p_email = input('Enter e-mail: ')
p_phone = input('Enter phone: ')
print_person_data(name=p_name, surname=p_surname, b_year=p_b_year, city=p_city, email=p_email, phone=p_phone)
