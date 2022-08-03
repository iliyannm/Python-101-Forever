def sum_of_digits(n):
    n_as_string = str(abs(n))
    final_number = 0

    for i in n_as_string:
        final_number += int(i)

    return final_number


tests = [
    (1325132435356, 43),
    (123, 6),
    (6, 6),
    (-10, 1)
]

for full_num, final_num in tests:
    if final_num == sum_of_digits(full_num):
        print(True)
    else:
        print(False)
