time = int(input('Enter time period in seconds: '))
hours = time // 3600
minutes = time % 3600 // 60
seconds = time % 60
# print('Time period: %02d:%02d:%02d' % (hours, minutes, seconds))
print(f'Time period: {hours:02}:{minutes:02}:{seconds:02}')
