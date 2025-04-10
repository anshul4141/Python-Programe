list = [5, 4, 6, 1, 3, 3, 2]
print("list = ", list)
list.append(7)
print("list = ", list)
print(list.count(8))
print(list.index(2))
list.remove(3)
print("list = ", list)
list.insert(0, 1)
print("list = ", list)

t = tuple(list)

print("list = ", t)
