from PuzzleInput import ReadInput
import numpy as np

pz_input = ReadInput(9).data
print(pz_input)
maps = np.array([np.array([int(y) for y in x]).reshape((10, 10)) for x in pz_input if x != ""])
maps = np.array([[[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
                  [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
                  [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
                  [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
                  [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]],
                 [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
                  [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
                  [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
                  [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
                  [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]])


def part_a():
    result = np.ones(maps.shape, dtype=bool)
    result[maps == 9] = False
    # right
    result[:, :, 1:] = np.logical_and((maps[:, :, 1:] - maps[:, :, :-1]) < 0, result[:, :, 1:])
    # left
    result[:, :, :-1] = np.logical_and((maps[:, :, :-1] - maps[:, :, 1:]) < 0, result[:, :, :-1])
    # top
    result[:, :-1, :] = np.logical_and((maps[:, :-1, :] - maps[:, 1:, :]) < 0, result[:, :-1, :])
    # bottom
    result[:, 1:, :] = np.logical_and((maps[:, 1:, :] - maps[:, :-1, :]) < 0, result[:, 1:, :])
    return np.sum(maps[result] + 1)


def part_b():
    pass


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
