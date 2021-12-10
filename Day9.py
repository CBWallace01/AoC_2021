import math

from PuzzleInput import ReadInput
import numpy as np

pz_input = ReadInput(9).data
print(pz_input)
maps = np.array([np.array([int(y) for y in x]) for x in pz_input if x != ""])
# maps = maps[0, :, :].reshape(1, 10, 10)
# maps = np.array([[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
#                  [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
#                  [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
#                  [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
#                  [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]])


def part_a():
    result = np.ones(maps.shape, dtype=bool)
    result[maps == 9] = False
    # right
    result[:, 1:] = np.logical_and((maps[:, 1:] - maps[:, :-1]) < 0, result[:, 1:])
    # left
    result[:, :-1] = np.logical_and((maps[:, :-1] - maps[:, 1:]) < 0, result[:, :-1])
    # top
    result[:-1, :] = np.logical_and((maps[:-1, :] - maps[1:, :]) < 0, result[:-1, :])
    # bottom
    result[1:, :] = np.logical_and((maps[1:, :] - maps[:-1, :]) < 0, result[1:, :])
    return np.sum(maps[result] + 1)


def part_b():
    result = np.ones(maps.shape, dtype=bool)
    result[maps == 9] = False
    basin_sizes = []
    for row in range(result.shape[0]):
        for col in range(result.shape[1]):
            if result[row, col]:
                visited = []
                edges = [(row, col)]
                while len(edges) > 0:
                    curr_row, curr_col = edges.pop()
                    if curr_row > 0 and result[curr_row-1, curr_col] and (curr_row-1, curr_col) not in edges:
                        edges.append((curr_row-1, curr_col))
                    if curr_row < maps.shape[0] - 1 and result[curr_row+1, curr_col] and (curr_row+1, curr_col) not in edges:
                        edges.append((curr_row+1, curr_col))
                    if curr_col > 0 and result[curr_row, curr_col-1] and (curr_row, curr_col-1) not in edges:
                        edges.append((curr_row, curr_col-1))
                    if curr_col < maps.shape[1] - 1 and result[curr_row, curr_col+1] and (curr_row, curr_col+1) not in edges:
                        edges.append((curr_row, curr_col+1))
                    visited.append((curr_row, curr_col))
                    result[curr_row, curr_col] = False
                basin_sizes.append(len(visited))
    basin_sizes.sort()
    return math.prod(basin_sizes[-3:])


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
