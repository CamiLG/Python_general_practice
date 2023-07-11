# Examples of while and for loops

count = 0
while count < 3:
    print(f'A condition is true, because {count} is minor to 3')
    count += 1
else:
    print("A condition turned false")

word = 'Hello'

for letter in word:
    print(letter)
else:
    print('End of for cicle')


# Example of break and continue usage
for letter in word:
    if letter == 'o':
        break
    print(f'{letter}')


for i in range(6):
    if i % 2 == 0:
        print(f'Value: {i}')

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Value: {i}')

