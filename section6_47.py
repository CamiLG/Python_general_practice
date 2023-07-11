month = int(input('Please enter the current month (1-12): '))
season = None
if month == 1 or month == 2 or month == 12:
    season = 'Winter'
elif 3 <= month < 6:
    season = 'Spring'
elif 6 <= month < 9:
    season = 'Summer'
elif 9 <= month < 12:
    season = 'Autumn'
else:
    season = 'Incorrect'
print(f'The season for month {month} is: {season}')