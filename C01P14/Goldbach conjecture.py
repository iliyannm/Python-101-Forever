def goldbach(n):
    combinations = []

    if n % 2 != 0:
        return None

    for i in range(2, (n // 2) + 1):
        is_prime = True

        number = n - i

        if number <= 1:
            break

        for j in range(2, number):
            if number % j == 0:
                is_prime = False
                break

        for k in range(2, i + 1):
            if i % k == 0 and i != k:
                is_prime = False
                break

        if is_prime:
            combinations.append((i, number))

        number = n

    return combinations


tests = [
    (4, [(2, 2)]),
    (6, [(3, 3)]),
    (8, [(3, 5)]),
    (10, [(3, 7), (5, 5)]),
    (100, [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]),
    (5, None)
]

for n, answer in tests:
    if answer == goldbach(n):
        print(True)
    else:
        print(False)
