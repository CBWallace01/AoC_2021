from PuzzleInput import ReadInput
import numpy as np

pz_input = ReadInput(3).data
print(pz_input)


def part_a():
    gamma = np.sum(np.array([np.array([int(x) for x in data]) for data in pz_input if data != ""]), axis=0)
    gamma[gamma < len(pz_input) // 2] = 0
    gamma[gamma >= len(pz_input) // 2] = 1
    epsilon = (~gamma.astype(bool)).astype(int)
    return gamma.dot(1 << np.arange(gamma.shape[-1] - 1, -1, -1)) * epsilon.dot(1 << np.arange(epsilon.shape[-1] - 1, -1, -1))


def part_b():
    common = np.array([np.array([int(x) for x in data]) for data in pz_input if data != ""])
    oxy = np.nonzero(common[:, 0] == (1 if np.sum(common[:, 0]) >= common.shape[0] / 2. else 0))[0]
    co = np.nonzero(common[:, 0] == (0 if np.sum(common[:, 0]) >= common.shape[0] / 2. else 1))[0]
    for i in range(1, common.shape[1]):
        if len(oxy) > 1:
            oxy = oxy[np.nonzero(common[oxy, i].flatten() == (1 if np.sum(common[oxy, i]) >= common[oxy].shape[0] / 2. else 0))[0]]
        if len(co) > 1:
            co = co[np.nonzero(common[co, i].flatten() == (0 if np.sum(common[co, i]) >= common[co].shape[0] / 2. else 1))[0]]
    return np.array([int(x) for x in common[oxy[0]]]).dot(1 << np.arange(len(common[oxy[0]]) - 1, -1, -1)) * \
           np.array([int(x) for x in common[co[0]]]).dot(1 << np.arange(len(common[co[0]]) - 1, -1, -1))


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
