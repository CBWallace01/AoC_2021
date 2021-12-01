from PuzzleInput import ReadInput
import numpy as np

pz_input = np.array([int(x) for x in ReadInput(1).data if x != ""])
print(pz_input)


def part_a():
    diffs = pz_input[1:] - pz_input[:-1]
    return np.count_nonzero(diffs > 0)


def part_b():
    diffs = (pz_input[1:-2] + pz_input[2:-1] + pz_input[3:]) - \
            (pz_input[:-3] + pz_input[1:-2] + pz_input[2:-1])
    return np.count_nonzero(diffs > 0)


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
