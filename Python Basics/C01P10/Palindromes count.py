def palindromes_count(n):
    palindromes_matches = 0

    for i in range(10, n + 1):
        if str(i) == str(i)[::-1]:
            palindromes_matches += 1

    return palindromes_matches


tests = [
    (10, 0),
    (20, 1),
    (101, 10),
    (200, 19),
    (43539, 525),
    (4247, 132),
    (48877, 577),
    (94012, 1029),
    (62560, 715),
    (92009, 1009),
    (63176, 721),
    (67409, 763),
    (62834, 718),
    (77420, 863),
    (92009, 1009),
    (99999, 1089)
]

for n, ans in  tests:
    if ans == palindromes_count(n):
        print(True)
    else:
        print(False)
