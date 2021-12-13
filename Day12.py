from PuzzleInput import ReadInput
import numpy as np
from collections import defaultdict

pz_input = ReadInput(12).data
print(pz_input)
# pz_input = ['start-A',
# 'start-b',
# 'A-c',
# 'A-b',
# 'b-d',
# 'A-end',
# 'b-end']


def part_a():
    cave_map = defaultdict(set)
    for connection in pz_input:
        if connection == '':
            continue
        pieces = connection.split('-')
        cave_map[pieces[0]].add(pieces[1])
        cave_map[pieces[1]].add(pieces[0])
    in_progress_paths = [['start']]
    complete_paths = []
    while len(in_progress_paths) > 0:
        curr = in_progress_paths.pop()
        for connection in cave_map[curr[-1]]:
            if connection == 'end':
                curr.append(connection)
                complete_paths.append(curr)
            elif connection.isupper() or (connection.islower() and connection not in curr):
                new_path = curr.copy()
                new_path.append(connection)
                in_progress_paths.append(new_path)
    return len(complete_paths)


def part_b():
    cave_map = defaultdict(set)
    for connection in pz_input:
        if connection == '':
            continue
        pieces = connection.split('-')
        cave_map[pieces[0]].add(pieces[1])
        cave_map[pieces[1]].add(pieces[0])
    in_progress_paths = [(['start'], False)]
    complete_paths = []
    while len(in_progress_paths) > 0:
        curr, used_small = in_progress_paths.pop()
        for connection in cave_map[curr[-1]]:
            if connection == 'start':
                continue
            elif connection == 'end':
                curr.append(connection)
                complete_paths.append(curr)
            elif connection.isupper():
                new_path = curr.copy()
                new_path.append(connection)
                in_progress_paths.append((new_path, used_small))
            elif connection.islower():
                if connection not in curr:
                    new_path = curr.copy()
                    new_path.append(connection)
                    in_progress_paths.append((new_path, used_small))
                elif not used_small:
                    new_path = curr.copy()
                    new_path.append(connection)
                    in_progress_paths.append((new_path, True))
    return len(complete_paths)


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
