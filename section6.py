# Exercise about control structures in Python
num_1 = int(input('Enter a value between 1 and 3: '))

if num_1 == 1:
    number_text = 'Number One'
elif num_1 == 2: 
    number_text = 'Number two'
elif num_1 == 3:
    number_text = 'Number three'
else:
    number_text = 'Value out of range'

print(f' Number is: {num_1} - {number_text}') 

condition = True

print('Condition true') if condition else print('Condition false')