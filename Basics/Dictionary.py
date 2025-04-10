d = {"name":"Ram", "surname":"Yadav", "age":18, "salary":4000.00}
print(len(d))
n = d["name"]

print(n)
print(d["surname"])
print(d["age"])
print(d["salary"])

print(d.get("age"))

k = d.keys()
print(k)
v = d.values()
print(v)