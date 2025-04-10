print("------simple function-------")
def sum(a, b):
    c = a + b
    return c


print(sum(5, 10))
print(sum(14, 15))
d = sum(2, 3)
print(d)

def multiply(a, b):
    c = a * b
    return c

i = multiply(2, 4)
print(i)

print("-----default argument function-------")
def sum(a, b = 5):
    c = a + b
    return c

print(sum(10))
print(sum(10, 2))

print("-------variable argument function-------")

def sumNum(a, *varg):
    t = a
    for n in varg:
        print(n)
        t = t + n
    return t

total = sumNum(5,2,3,4,5,2)
print(total)


