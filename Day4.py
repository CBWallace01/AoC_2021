from PuzzleInput import ReadInput
import numpy as np

pz_input = ReadInput(4).data
# pz_input = ["7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
# "",
# "22 13 17 11  0",
# "8  2 23  4 24",
# "21  9 14 16  7",
# "6 10  3 18  5",
# "1 12 20 15 19",
# "",
# "3 15  0  2 22",
# "9 18 13 17  5",
# "19  8  7 25 23",
# "20 11 10 24  4",
# "14 21 16 12  6",
# "",
# "14 21 17 24  4",
# "10 16 15  9 19",
# "18  8 23 26 20",
# "22 11 13  6  5",
# "2  0 12  3  7"]
print(pz_input)
numbers = [int(x) for x in pz_input[0].split(",")]
boards = []
i = -1
for j in range(1, len(pz_input)):
    if pz_input[j] == "":
        i += 1
    else:
        if len(boards) < i + 1:
            boards.append(np.array([int(x) for x in pz_input[j].split(" ") if x != ""]))
        else:
            boards[i] = np.vstack((boards[i], [int(x) for x in pz_input[j].split(" ") if x != ""]))
boards = np.array(boards)


def part_a():
    a_boards = boards.copy()
    for num in numbers:
        a_boards[a_boards == num] = -1
        rows = np.argwhere(np.sum(a_boards, axis=1) == -5)
        cols = np.argwhere(np.sum(a_boards, axis=2) == -5)
        if rows.shape[0] or cols.shape[0]:
            a_boards[a_boards == -1] = 0
            return num * (np.sum(a_boards[rows[0, 0]]) if rows.shape[0] > 0 else np.sum(a_boards[cols[0, 0]]))


def part_b():
    b_boards = boards.copy()
    idx = set(np.arange(b_boards.shape[0]))
    to_watch = None
    for num in numbers:
        b_boards[b_boards == num] = -1
        rows = np.argwhere(np.sum(b_boards, axis=1) == -5)
        cols = np.argwhere(np.sum(b_boards, axis=2) == -5)
        winners = set([x for x in rows[:, 0]] + [x for x in cols[:, 0]])
        if to_watch is not None and to_watch in winners:
            b_boards[b_boards == -1] = 0
            return num * np.sum(b_boards[to_watch])
        if to_watch is None and len(winners) == len(idx) - 1:
            to_watch = list(idx - winners)[0]


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
