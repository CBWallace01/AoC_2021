from PuzzleInput import ReadInput
import numpy as np

pz_input = np.array([int(x) for x in ReadInput(7).data[0].split(",") if x != ""])
# pz_input = np.array([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])
# print(pz_input)


def part_a():
    return np.sum(np.abs(pz_input - np.median(pz_input)))


def part_b():
    curr = np.median(pz_input)
    best = np.sum([(abs(x - curr) ** 2 / 2) + (abs(x - curr) / 2) for x in pz_input])
    direction = 1 if np.sum([(abs(x - (curr + 1)) ** 2 / 2) + (abs(x - (curr + 1)) / 2) for x in pz_input]) < best else -1
    i = 1
    next_num = np.sum([(abs(x - (curr + (direction * i))) ** 2 / 2) + (abs(x - (curr + (direction * i))) / 2) for x in pz_input])
    while next_num < best:
        best = next_num
        i += 1
        next_num = np.sum([(abs(x - (curr + (direction * i))) ** 2 / 2) + (abs(x - (curr + (direction * i))) / 2) for x in pz_input])
    return best


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
