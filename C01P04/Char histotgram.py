def char_histogram(string):
    dictionary = {}

    for x in string:
        if x not in dictionary:
            dictionary[x] = 0
        dictionary[x] += 1

    return dictionary


tests = [
    ("", {}),
    ("    ", {' ': 4}),
    ("Python!", {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1}),
    ("AAAAaaa!!!", {'A': 4, 'a': 3, '!': 3}),
    ("Some very long string here with different casing", {
    'S': 1,
    'o': 2,
    'm': 1,
    'e': 6,
    ' ': 7,
    'v': 1,
    'r': 4,
    'y': 1,
    'l': 1,
    'n': 4,
    'g': 3,
    's': 2,
    't': 3,
    'i': 4,
    'h': 2,
    'w': 1,
    'd': 1,
    'f': 2,
    'c': 1,
    'a': 1
    })
]

for input, answer in tests:
    if answer == char_histogram(input):
        print(True)
    else:
        print(False)
