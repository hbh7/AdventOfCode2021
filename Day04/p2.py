class Board:
    def __init__(self):
        self.spots = [[] for _ in range(5)]
        self.hits = [[False]*5 for _ in range(5)]

    def add_row(self, index, row):
        self.spots[index] = row

    def mark(self, n):
        for y in range(5):
            for x in range(5):
                if self.spots[y][x] == n:
                    self.hits[y][x] = True
                    break

    def has_won(self):
        # Check for horizontal wins
        for y in range(5):
            c = 0
            for x in range(5):
                if self.hits[y][x]:
                    c += 1
            if c == 5:
                return True
        # Check for vertical wins
        for x in range(5):
            c = 0
            for y in range(5):
                if self.hits[y][x]:
                    c += 1
            if c == 5:
                return True

    def get_score(self):
        s = 0
        for y in range(5):
            for x in range(5):
                if not self.hits[y][x]:
                    s += self.spots[y][x]
        return s


if __name__ == "__main__":
    inputfile = open("input.txt")

    numbers = []
    boards = []

    first_line = True
    board_index = -1
    board_row_index = 0
    for line in inputfile:
        if first_line:
            n = line.split(",")
            numbers = list(map(int, n))
            first_line = False
        elif line == "\n":
            board_index += 1
            board_row_index = 0
            boards.append(Board())
        else:
            # Continued board definition
            n = line.split()
            n2 = list(map(int, n))
            boards[board_index].add_row(board_row_index, n2)
            board_row_index += 1

    # Call numbers
    for number in numbers:
        board_len = len(boards)
        i = 0
        while i < board_len:
            boards[i].mark(number)
            if boards[i].has_won():
                if len(boards) > 1:
                    boards.remove(boards[i])
                    i -= 1
                    board_len -= 1
                else:
                    score = boards[i].get_score() * number
                    print(score)
                    exit(0)
            i += 1

