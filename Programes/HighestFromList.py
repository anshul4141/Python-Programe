# Find the largest number in list
list = [56, 89, 41, 32, 52, 879, 41]

b = list[0]

l = len(list)

print("lenght of list = ", l)

for i in range(l):
    if list[i] > b:
        b = list[i]

print("Largest No is:", b)
