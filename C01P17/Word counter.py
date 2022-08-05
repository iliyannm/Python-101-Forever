def left_down_diagonal(mat, word, letter, row, col, index_pairs):
    found = False
    while row + 1 < len(mat) and col - 1 >= 0:
        row += 1
        col -= 1
        letter += mat[row][col]
        if letter == word:
            found = True
            break

    if found:
        for pair in index_pairs:
            if row == pair[0] + (len(word) - 1) and col == pair[1] - (len(word) - 1):
                return False
        return True

    return False


def left_horizontal(mat, word, letter, row, col, index_pairs):
    found = False
    while col - 1 >= 0:
        col -= 1
        letter += mat[row][col]
        if letter == word:
            found = True
            break

    if found:
        for pair in index_pairs:
            if row == pair[0] and col == pair[1] - (len(word) - 1):
                return False
        return True

    return False


def left_up_diagonal(mat, word, letter, row, col, index_pairs):
    found = False
    while row - 1 >= 0 and col - 1 >= 0:
        row -= 1
        col -= 1
        letter += mat[row][col]
        if letter == word:
            found = True
            break

    if found:
        for pair in index_pairs:
            if row == pair[0] - (len(word) - 1) and col == pair[1] - (len(word) - 1):
                return False
        return True

    return False


def upper_vertical(mat, word, letter, row, col, index_pairs):
    found = False
    while row - 1 >= 0:
        row -= 1
        letter += mat[row][col]
        if letter == word:
            found = True
            break

    if found:
        for pair in index_pairs:
            if row == pair[0] - (len(word) - 1) and col == pair[1]:
                return False
        return True

    return False


def right_up_diagonal(mat, word, letter, row, col, index_pairs):
    found = False
    while row - 1 >= 0 and col + 1 < len(mat[row]):
        row -= 1
        col += 1
        letter += mat[row][col]
        if letter == word:
            found = True
            break

    if found:
        for pair in index_pairs:
            if row == pair[0] - (len(word) - 1) and col == pair[1] + (len(word) - 1):
                return False
        return True

    return False


def right_horizontal(mat, word, letter, row, col, index_pairs):
    found = False
    while col + 1 < len(mat[row]):
        col += 1
        letter += mat[row][col]
        if letter == word:
            found = True
            break

    if found:
        for pair in index_pairs:
            if row == pair[0] and col == pair[1]  + (len(word) - 1) :
                return False
        return True

    return False


def right_down_horizontal(mat, word, letter, row, col, index_pairs):
    found = False
    while row + 1 < len(mat) and col + 1 < len(mat[row]):
        row += 1
        col += 1
        letter += mat[row][col]
        if letter == word:
            found = True
            break

    if found:
        for pair in index_pairs:
            if row == pair[0] + (len(word) - 1) and col == pair[1] + (len(word) - 1):
                return False
        return True

    return False


def down_vertical(mat, word, letter, row, col, index_pairs):
    found = False
    while row + 1 < len(mat):
        row += 1
        letter += mat[row][col]
        if letter == word:
            found = True
            break

    if found:
        for pair in index_pairs:
            if row == pair[0] + (len(word) - 1) and col == pair[1]:
                return False
        return True

    return False


def word_counter(matrix, word):
    initial_letter = word[0]
    counter = 0
    found_indexes = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == initial_letter:
                if left_down_diagonal(matrix, word, initial_letter, i, j, found_indexes):
                    counter += 1
                    found_indexes.append((i, j))
                if left_horizontal(matrix, word, initial_letter, i, j, found_indexes):
                    counter += 1
                    found_indexes.append((i, j))
                if left_up_diagonal(matrix, word, initial_letter, i, j, found_indexes):
                    counter += 1
                    found_indexes.append((i, j))
                if upper_vertical(matrix, word, initial_letter, i, j, found_indexes):
                    counter += 1
                    found_indexes.append((i, j))
                if right_up_diagonal(matrix, word, initial_letter, i, j, found_indexes):
                    counter += 1
                    found_indexes.append((i, j))
                if right_horizontal(matrix, word, initial_letter, i, j, found_indexes):
                    counter += 1
                    found_indexes.append((i, j))
                if right_down_horizontal(matrix, word, initial_letter, i, j, found_indexes):
                    counter += 1
                    found_indexes.append((i, j))
                if down_vertical(matrix, word, initial_letter, i, j, found_indexes):
                    counter += 1
                    found_indexes.append((i, j))

    return counter

word = "ivan"
matrix = [
    ["i", "v", "a", "n"],
    ["e", "v", "n", "h"],
    ["i", "n", "a", "v"],
    ["m", "v", "v", "n"],
    ["q", "r", "i", "t"]
]

print(word_counter(matrix, word) == 3)

# word = "actually"
# matrix = [
#     ["i", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z", "o", "y", "m"],  # noqa
#     ["e", "v", "n", "h", "t", "r", "x", "e", "k", "y", "d", "a", "i", "l", "c"],  # noqa
#     ["i", "a", "c", "t", "u", "a", "l", "l", "y", "m", "c", "x", "r", "l", "e"],  # noqa
#     ["m", "v", "c", "n", "p", "u", "a", "m", "n", "t", "l", "u", "e", "a", "a"],  # noqa
#     ["q", "r", "i", "t", "w", "e", "a", "q", "u", "p", "r", "x", "t", "u", "z"],  # noqa
#     ["p", "e", "a", "c", "t", "u", "a", "l", "l", "y", "w", "p", "y", "t", "m"],  # noqa
#     ["o", "y", "h", "t", "r", "e", "l", "u", "f", "p", "q", "n", "z", "c", "s"],  # noqa
#     ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e", "q", "a", "r"]   # noqa
# ]
# print(word_counter(matrix, word) == 4)
#
# word = "madam"
# matrix = [
#     ["z", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z"],
#     ["e", "v", "m", "h", "t", "r", "x", "e", "k", "y", "m", "a"],
#     ["i", "a", "c", "a", "u", "a", "l", "l", "y", "a", "c", "x"],
#     ["m", "v", "c", "n", "d", "u", "a", "m", "d", "t", "l", "u"],
#     ["q", "t", "i", "t", "w", "a", "a", "a", "u", "p", "r", "x"],
#     ["p", "e", "m", "a", "d", "a", "m", "l", "l", "y", "w", "p"],
#     ["o", "y", "h", "t", "e", "e", "l", "u", "f", "p", "q", "n"],
#     ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e"]
# ]
#
# print(word_counter(matrix, word) == 3)