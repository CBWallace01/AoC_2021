import time

from PuzzleInput import ReadInput
from collections import defaultdict
import numpy as np

pz_input = np.array([int(x) for x in ReadInput(6).data[0].split(',') if x != ""])
print(pz_input)


def part_a():
    fish = pz_input.copy()
    for _ in range(80):
        fish -= 1
        new_fish = np.count_nonzero(fish == -1)
        if new_fish > 0:
            fish = np.hstack((fish, np.ones(new_fish) * 8))
            fish[fish == -1] = 6
    return fish.shape[0]


def part_b():
    fish = defaultdict(int)
    num_fish = pz_input.shape[0]
    for f in pz_input:
        fish[f] += 1
    for i in range(256):
        if i + 7 < 256:
            fish[i+7] += fish[i]
        if i + 9 < 256:
            fish[i+9] += fish[i]
        num_fish += fish[i]
    return num_fish


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
