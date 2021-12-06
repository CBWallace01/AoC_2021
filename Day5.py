from PuzzleInput import ReadInput
import numpy as np

pz_input = ReadInput(5).data
lines = None
for line in pz_input:
    if line == "":
        continue
    pairs = line.split(' -> ')
    start = [int(x) for x in pairs[0].split(',')]
    end = [int(x) for x in pairs[1].split(',')]
    new_line = np.array(start + end)
    if lines is None:
        lines = new_line
    else:
        lines = np.vstack((lines, new_line))
print(pz_input)


def part_a():
    a_lines = lines[np.logical_or(lines[:, 0] == lines[:, 2], lines[:, 1] == lines[:, 3])]
    vent_map = np.zeros((max(np.max(a_lines[:, 0]), np.max(a_lines[:, 2])) + 1, max(np.max(a_lines[:, 1]), np.max(a_lines[:, 3])) + 1))
    for line in a_lines:
        if line[0] == line[2]:
            for col in range(min(line[1], line[3]), max(line[1], line[3]) + 1):
                vent_map[line[0], col] += 1
        else:
            for row in range(min(line[0], line[2]), max(line[0], line[2]) + 1):
                vent_map[row, line[1]] += 1
    return np.count_nonzero(vent_map >= 2)


def part_b():
    vent_map = np.zeros((max(np.max(lines[:, 0]), np.max(lines[:, 2])) + 1, max(np.max(lines[:, 1]), np.max(lines[:, 3])) + 1))
    for line in lines:
        if line[0] == line[2]:
            for col in range(min(line[1], line[3]), max(line[1], line[3]) + 1):
                vent_map[line[0], col] += 1
        elif line[1] == line[3]:
            for row in range(min(line[0], line[2]), max(line[0], line[2]) + 1):
                vent_map[row, line[1]] += 1
        else:
            row_dir = 1 if line[2] > line[0] else -1
            col_dir = 1 if line[3] > line[1] else -1
            coords = list(zip(range(line[0], line[2] + row_dir, row_dir), range(line[1], line[3] + col_dir, col_dir)))
            for coord in coords:
                vent_map[coord] += 1
    return np.count_nonzero(vent_map >= 2)


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
