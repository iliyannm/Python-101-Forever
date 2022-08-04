def prime_factorization(n):
    dict = {}
    list = []
    number = n
    divider = 2

    while number != 1:
        if int(number) % divider == 0:
            if not divider in dict:
                dict[divider] = 0
            dict[divider] += 1
            number /= divider
            divider = 2
        else:
            divider += 1

    for k, v in dict.items():
        list.append((k, v))

    return list


tests = [
    (2, [(2, 1)]),
    (4, [(2, 2)]),
    (10, [(2, 1), (5, 1)]),  # This is 2^1 * 5^1
    (14, [(2, 1), (7, 1)]),
    (356, [(2, 2), (89, 1)]),
    (89, [(89, 1)]),  # 89 is a prime number
    (1000, [(2, 3), (5, 3)])
]


for n, expected in tests:
    if expected == prime_factorization(n):
        print(True)
    else:
        print(False)
