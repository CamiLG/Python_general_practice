# Exercises with functions in python

def my_function(name, last_name, phone, age):
    print(f'''
    Name: {name}
    Lastname: {last_name}
    Phone: {phone}
    Age: {age}
    ''')

my_function('Juan', 'Perez', 2213333344, 25)

def perimeter(a, b):

    return (a + b) * 2

print(f'The perimeter of the figure is: {perimeter(3,5)}') 