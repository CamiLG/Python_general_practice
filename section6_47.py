month = int(input('Please enter the current month (1-12)'))
season = None
if month == 1 or month == 2 or month == 12:
    season = 'Winter'
elif month >= 3 and month <= 5:
    season = 'Spring'
elif month >= 6 and month <= 8:
    season = 'Autumn'
else:
    season = 'Incorrect'
print(f'The season for month {month} is: {season}')