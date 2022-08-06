import random


class Minesweeper:
    matrix = []

    def generate_board(self, num_rows, num_cols, num_bombs):
        bombs_indexes = []
        range_rows = num_rows - 1
        range_cols = num_cols - 1

        for k in range(num_bombs):
            bomb_row = random.randint(0, range_rows)
            bomb_col = random.randint(0, range_cols)
            bombs_indexes.append((bomb_row, bomb_col))

        for i in range(num_rows):
            new_row = []
            for j in range(num_cols):
                new_row.append(0)
            self.matrix.append(new_row)

        for bomb in bombs_indexes:
            for p in range(len(self.matrix)):
                for t in range(len(self.matrix[p])):
                    if bomb[0] == p and bomb[1] == t:
                        self.matrix[p][t] = 9

        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[r])):
                if self.matrix[r][c] == 9:
                    continue

                # previous row
                if r - 1 >= 0:
                    if c - 1 >= 0:
                        if self.matrix[r - 1][c - 1] == 9:
                            self.matrix[r][c] += 1
                    if self.matrix[r - 1][c] == 9:
                        self.matrix[r][c] += 1
                    if c + 1 < len(self.matrix[r]):
                        if self.matrix[r - 1][c + 1] == 9:
                            self.matrix[r][c] += 1

                # the same row
                if c - 1 >= 0:
                    if self.matrix[r][c - 1] == 9:
                        self.matrix[r][c] += 1
                if c + 1 < len(self.matrix[r]):
                    if self.matrix[r][c + 1] == 9:
                        self.matrix[r][c] += 1

                # next row
                if r + 1 < len(self.matrix):
                    if c - 1 >= 0:
                        if self.matrix[r + 1][c - 1] == 9:
                            self.matrix[r][c] += 1
                    if self.matrix[r + 1][c] == 9:
                        self.matrix[r][c] += 1
                    if c + 1 < len(self.matrix[r]):
                        if self.matrix[r + 1][c + 1] == 9:
                            self.matrix[r][c] += 1

        print(self.matrix)


Minesweeper().generate_board(num_rows=4, num_cols=5, num_bombs=6)


# [0, 1, 2, 9, 1]
# [1, 3, 9, 5, 3]
# [1, 9, 9, 9, 9]
# [1, 2, 3, 3, 2]
