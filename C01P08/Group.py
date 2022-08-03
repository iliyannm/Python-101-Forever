def group(items):
    result = []
    current_list = []

    if len(items) - 1 == 0:
        result.append(items)

    for i in range(len(items) - 1):
        current_list.append(items[i])

        if items[i] != items[i + 1]:
            result.append(current_list)
            current_list = []

        if i == len(items) - 2:
            current_list.append(items[i + 1])
            result.append(current_list)

    return result


tests = [
    ([1, 1, 1, 2, 3, 1, 1], [[1, 1, 1], [2], [3], [1, 1]]),
    ([1, 2, 1, 2, 3, 3], [[1], [2], [1], [2], [3, 3]]),
    ([1, 2, 1, 2, 3, 4], [[1], [2], [1], [2], [3], [4]]),
    ([1, 2, 1, 2, 3, 4, 5, 6, 7], [[1], [2], [1], [2], [3], [4], [5], [6], [7]]),
    ([1, 2, 1, 2, 3, 4, 4, 4], [[1], [2], [1], [2], [3], [4, 4, 4]]),
    ([], []),
    ([1], [[1]]),
    ([1, 1, 1, 1], [[1, 1, 1, 1]])
]

for list, answer in tests:
    if answer == group(list):
        print(True)
    else:
        print(False)
