n = 123
temp = n
rn = 0

while temp > 0:
    r = temp % 10
    rn = rn * 10 + r
    temp = temp // 10

print("rn = ", rn)

if n == rn:
    print("this is palindrome no")
else:
    print("this is not palindrome no")