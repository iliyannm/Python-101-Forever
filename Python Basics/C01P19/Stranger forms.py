def stranger_forms(cinema_layout):
    possible_configurations = []
    result = []

    copied_cinema_scheme = cinema_layout.copy()
    copied_cinema_scheme = [list(m) for m in copied_cinema_scheme]
    failed = False

    for r in range(len(copied_cinema_scheme)):
        for c in range(len(copied_cinema_scheme[r])):
            if copied_cinema_scheme[r][c] == '.':
                # A
                copied_cinema_scheme[r][c] = 'A'

                # B
                if r - 1 >= 0:
                    if copied_cinema_scheme[r - 1][c] == '.':
                        copied_cinema_scheme[r - 1][c] = 'B'
                    else:
                        failed = True
                else:
                    failed = True

                # F
                if c + 1 < len(copied_cinema_scheme[r]):
                    if copied_cinema_scheme[r][c + 1] == '.':
                        copied_cinema_scheme[r][c + 1] = 'F'
                    else:
                        failed = True
                else:
                    failed = True

                # C
                if r - 2 >= 0:
                    if copied_cinema_scheme[r - 2][c] == '.':
                        copied_cinema_scheme[r - 2][c] = 'C'
                    else:
                        failed = True
                else:
                    failed = True

                # D
                if r -2 >= 0 and c + 1 < len(copied_cinema_scheme[r]):
                    if copied_cinema_scheme[r - 2][c + 1] == '.':
                        copied_cinema_scheme[r - 2][c + 1] = 'D'
                    else:
                        failed = True
                else:
                    failed = True

                # E
                if r - 3 >= 0 and c + 1 < len(copied_cinema_scheme[r]):
                    if copied_cinema_scheme[r - 3][c + 1] == '.':
                        copied_cinema_scheme[r - 3][c + 1] = 'E'
                    else:
                        failed = True
                else:
                    failed = True

                # G
                if r - 3 >= 0:
                    if copied_cinema_scheme[r - 3][c] == '.':
                        copied_cinema_scheme[r - 3][c] = 'G'
                    else:
                        failed = True
                else:
                    failed = True

            else:
                failed = True

            if failed:
                failed = False
            else:
                possible_configurations.append(copied_cinema_scheme)

            copied_cinema_scheme = cinema_layout.copy()
            copied_cinema_scheme = [list(m) for m in copied_cinema_scheme]

    for k in range(len(possible_configurations)):
        current_answer = []
        for p in range(len(possible_configurations[k])):
            current_answer.append(''.join(possible_configurations[k][p]))
        result.append(current_answer)

    return result


answers = [[
        '..*GE.*.**',
        '...CD**...',
        '*.*B..*..*',
        '.**AF..*.*',
        '...*..*.*.',
        '.***...*..',
        '*......*.*',
        '.....**..*',
        '..*.*.*..*',
        '***.*.**..'],

        [
        '..*...*.**',
        '.....**...',
        '*.*.GE*..*',
        '.**.CD.*.*',
        '...*B.*.*.',
        '.***AF.*..',
        '*......*.*',
        '.....**..*',
        '..*.*.*..*',
        '***.*.**..'],

        [
        '..*...*.**',
        '.....**...',
        '*.*...*..*',
        '.**.GE.*.*',
        '...*CD*.*.',
        '.***B..*..',
        '*...AF.*.*',
        '.....**..*',
        '..*.*.*..*',
        '***.*.**..']
        ]

if stranger_forms(
['..*...*.**',
 '.....**...',
 '*.*...*..*',
 '.**....*.*',
 '...*..*.*.',
 '.***...*..',
 '*......*.*',
 '.....**..*',
 '..*.*.*..*',
 '***.*.**..']) == answers:
    print(True)
else:
    print(False)