def group(items):
    result = []
    index = 0

    while index < len(items):
        current_group = [items[index]]

        lookup_index = index + 1

        while lookup_index < len(items) and items[index] == items[lookup_index]:
            current_group.append(items[lookup_index])
            index += 1
            lookup_index = index + 1

        result.append(current_group)
        index += 1

    return result


KEYPAD = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz"
}


def numbers_to_message(pressed_sequence):
    grouped_sequence = group(pressed_sequence)
    messagge = []
    is_capital = False

    for current_group in grouped_sequence:
        key = current_group[0]
        time_pressed = len(current_group)

        if key == 0:
            messagge.append(' ' * time_pressed)

        elif key == -1:
            continue

        elif key == 1:
            is_capital = True

        else:
            letter = KEYPAD[key][(time_pressed - 1) % len(KEYPAD[key])]

            if is_capital:
                is_capital = False
                messagge.append(letter.upper())
                continue

            messagge.append(letter)

    return ''.join(messagge)


tests = [
    (
        [0, 0, 0, 0],
        "    "
    ),
    (
        [2, -1, 2, 2, -1, 2, 2, 2],
        "abc"
    ),
    (
        [2, 2, 2, 2],
        "a"
    ),
    (
        [1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2],
        "Ivo e Panda"
    ),
    (
        [2, 3, 4, 5, 6, 7, 8, 9],
        "adgjmptw"
    ),
    (
        [2, -1, 3,-1, 4, -1, 5, -1, 6, -1, 7, -1, 8, -1, 9],
        "adgjmptw"
    ),
    (
        [0, -1, 0, -1, 0, -1, 0],
        "    "
    ),
    (
        [2, 2, 2, -1, 2],
        "ca"
    ),
]

for sequence, answer in tests:
    if answer == numbers_to_message(sequence):
        print(True)
    else:
        print(False)
