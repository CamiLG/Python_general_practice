# Assigments in Python

var = 10
print(var)

var = var + 1 
print(var)

var += 1
print(var)

var -= 2
print(var)

var *= 2
print(f'{var}')

var /= 2
print(f'{var}')

a = 10
result = var == a
print(f'{var}')
print(f'{a}')
print(f'var and a are equal: {result}')

a = int(input('Enter a number value: '))
if a % 2 == 0:
    print(f'The number {a} is pair')
else:
    print(f'The value {a} is not pair')

#Multiple assigments
b = c = a % 2 == 0
print(b and c)
