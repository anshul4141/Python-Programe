def isPrime(*n):
    count = 0
    for a in n:
        for i in range(2, a):
            if a % i == 0:
              count = count + 1

        if count > 0:
            print(a, "is not prime no")
            count = 0
        else:
            print(a, "is prime no")

isPrime(2, 3, 4, 5, 7, 8, 6)
