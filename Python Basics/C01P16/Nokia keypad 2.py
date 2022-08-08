SEQUENCES = {
    "a": [2],
    "b": [2, 2],
    "c": [2, 2, 2],
    "d": [3],
    "e": [3, 3],
    "f": [3, 3, 3],
    "g": [4],
    "h": [4, 4],
    "i": [4, 4, 4],
    "j": [5],
    "k": [5, 5],
    "l": [5, 5, 5],
    "m": [6],
    "n": [6, 6],
    "o": [6, 6, 6],
    "p": [7],
    "q": [7, 7],
    "r": [7, 7, 7],
    "s": [7, 7, 7, 7],
    "t": [8],
    "u": [8, 8],
    "v": [8, 8, 8],
    "w": [9],
    "x": [9, 9],
    "y": [9, 9, 9],
    "z": [9, 9, 9, 9],
    " ": [0]
}


def message_to_numbers(message):
    number_sequence = []

    for i in range(len(message)):
        letter = message[i]

        if letter.isupper():
            number_sequence.append(1)
            letter = letter.lower()

        current_sequence = SEQUENCES[letter]

        number_sequence.extend(current_sequence)

        if i != len(message) - 1:
            if SEQUENCES[letter][0] == SEQUENCES[(message[i + 1]).lower()][0]:
                number_sequence.append(-1)

    return number_sequence

tests = [
    ("abc", [2, -1, 2, 2, -1, 2, 2, 2]),
    ("a", [2]),
    ("Ivo e Panda", [1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2]),  # noqa
    ("aabbcc", [2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2])
]


for message, expected in tests:
    if expected == message_to_numbers(message):
        print(True)
    else:
        print(False)