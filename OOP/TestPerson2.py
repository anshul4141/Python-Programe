from Person import *

# First person input
p = Person()
name1 = input("Enter name for person 1: ")
address1 = input("Enter address for person 1: ")
p.setName(name1)
p.setAddress(address1)

print(p.getName())
print(p.getAddress())

print("-------------")

# Second person input
p1 = Person()
name2 = input("Enter name for person 2: ")
address2 = input("Enter address for person 2: ")
p1.setName(name2)
p1.setAddress(address2)

print(p1.getName())
print(p1.getAddress())