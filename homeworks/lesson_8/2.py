class MyZeroDivisionError(ZeroDivisionError):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    divider = float(input('Enter divider: '))
    if divider != 0:
        print(f'5.0 / {divider} = ', 5.0 / divider)
    else:
        raise MyZeroDivisionError("You can't divide by zero!!!")
except MyZeroDivisionError as mzde:
    print(mzde)
