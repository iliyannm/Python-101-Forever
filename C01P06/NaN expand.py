def nan_expand(times):
    result = ''

    if times == 0:
        return result

    for i in range(times):
        result += 'Not a '

    result += 'NaN'

    return result


tests = [
    (0, ""),
    (1, "Not a NaN"),
    (2, "Not a Not a NaN"),
    (3, "Not a Not a Not a NaN")
]

for times, answer in tests:
    if answer == nan_expand(times):
        print(True)
    else:
        print(False)
