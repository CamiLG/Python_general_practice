# Lists practice

names = ['Juan', 'Carla', 'Ricardo', 'Maria', 0, 100, True]
print(names[0])

for name in names:
    print(name)

# Not including the last index
print(names[0:2]) 

# Not including the last index
print(names[:3]) 

# Print from first index to the end of the list
print(names[2:])

names[2] = 'Lisa'

for name in names:
    print(name)