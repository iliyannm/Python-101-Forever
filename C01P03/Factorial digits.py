def fact(n):
    result = 1

    for x in range(1, n + 1):
        result *= x

    return result


def fact_digits(n):
    n_as_string = str(abs(n))
    final_number = 0

    for i in n_as_string:
        final_number += fact(int(i))

    return final_number


tests = [
    (101, 3),
    (111, 3),
    (145, 145),
    (999, 1088640)
]

for initial_num, final_num in tests:
    if final_num == fact_digits(initial_num):
        print(True)
    else:
        print(False)
