from enum import Enum


class Monotonicity(Enum):
    INCREASING = 1
    DECREASING = 2
    NONE = 3


def increasing_or_decreasing(ns):
    is_increasing = False
    is_decreasing = False

    for i in range(len(ns) - 1):
        if ns[i] < ns[i + 1]:
            is_increasing = True

        elif ns[i] > ns[i + 1]:
            is_decreasing = True

        else:
            return Monotonicity.NONE

    if is_increasing == is_decreasing:
        return Monotonicity.NONE

    elif is_increasing is True and is_decreasing is False:
        return Monotonicity.INCREASING

    elif is_increasing is False and is_decreasing is True:
        return Monotonicity.DECREASING


tests = [
    ([1, 2, 3, 4, 5], Monotonicity.INCREASING),
    ([5, 6, -10], Monotonicity.NONE),
    ([1, 1, 1, 1], Monotonicity.NONE),
    ([9, 8, 7, 6], Monotonicity.DECREASING),
    ([], Monotonicity.NONE),
    ([1], Monotonicity.NONE),
    ([1, 100], Monotonicity.INCREASING),
    ([1, 100, 100], Monotonicity.NONE),
    ([100, 1], Monotonicity.DECREASING),
    ([100, 1, 1], Monotonicity.NONE),
    ([100, 1, 2], Monotonicity.NONE)
]

for list, answer in tests:
    if answer == increasing_or_decreasing(list):
        print(True)
    else:
        print(False)
