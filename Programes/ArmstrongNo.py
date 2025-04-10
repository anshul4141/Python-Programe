n = 153
temp = n
r = 0
rn = 0

while temp > 0:
    r = temp % 10
    rn = rn + r * r * r
    temp = temp // 10

print("rn = ", rn)

if n == rn:
    print("this is armstrong no")
else:
    print("this is not armstrong no")