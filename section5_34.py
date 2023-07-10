#Section to implement logical operations that can be improved

value = int(input('Enter a number: '))
min = 0
max = 20

in_range = value >= min and value <= max
if in_range:
    print(f'The value {value} is in range')
else:
    print(f'The value entered is not in range')