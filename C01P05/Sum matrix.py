def sum_matrix(m):
    result = 0

    for i in range(len(m)):
        for j in range(len(m[i])):
            result += m[i][j]

    return result


tests = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 45),
    ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
    ([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], 55)
]

for matrix, answer in tests:
    if answer == sum_matrix(matrix):
        print(True)
    else:
        print(False)
