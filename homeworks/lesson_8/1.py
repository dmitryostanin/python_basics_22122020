class Date:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def date_to_ints(cls, date: str):
        dd, mm, yy = date.split('-')
        dd = int(dd)
        mm = int(mm)
        yy = int(yy)
        return dd, mm, yy

    @staticmethod
    def validate(date: tuple):
        try:
            dd, mm, yy = date
            month_max_days_amount = [31, 28 if yy % 4 else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if yy >= 0 and 0 < mm <= 12 and 0 < dd <= month_max_days_amount[mm - 1]:
                return True
            else:
                raise ValueError('ValueError!!!')
        except ValueError as ve:
            print(ve, end=' ')
            return False


d1 = Date('29-02-2020')
d2 = Date('29-02-2021')
print(f'Date {d1.date} is valid!' if Date.validate(Date.date_to_ints(d1.date)) else f'Date {d1.date} is not valid!')
print(f'Date {d2.date} is valid!' if Date.validate(Date.date_to_ints(d2.date)) else f'Date {d2.date} is not valid!')
