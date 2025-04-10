num = 7
count = 0

for i in range(2, num):
    if num % i == 0:
        count = count + 1

if count == 0:
    print(num,"is prime no")
else:
    print(num,"is not prime no")
