def secondLargest(list):

    first = list[0]
    second = 0

    l = len(list)

    print("length of list = ", l)

    for i in range(l):
        if list[i] > first:
            second = first
            first = list[i]
        if list[i] < first and list[i] > second:
            second = list[i]

    print("Second Largest No is:", second)

list = [56, 89, 99, 100, 52, 879, 41]
secondLargest(list)


