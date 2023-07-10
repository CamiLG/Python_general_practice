# Section to implement logical operations that can be improved

value = int(input('Enter a number: '))
min = 0
max = 20
# Try to improve with other function that compares the value to a variable range and returns the comparison
in_range = value >= min and value <= max
if in_range:
    print(f'The value {value} is in range')
else:
    print(f'The value entered is not in range')

num_1 = int(input('Enter the first value: '))
num_2 = int(input('Enter the second value: '))

if num_1 > num_2:
    print('Number 1 is major than number 2')
else:
    print('Number 2 is major than number 1')