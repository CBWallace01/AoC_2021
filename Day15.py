from PuzzleInput import ReadInput
import numpy as np
import heapq

pz_input = np.array([[int(y) for y in x] for x in ReadInput(15).data if x != ""])
print(pz_input)
# pz_input = np.array([[1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
#                      [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
#                      [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
#                      [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
#                      [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
#                      [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
#                      [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
#                      [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
#                      [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
#                      [2, 3, 1, 1, 9, 4, 4, 5, 8, 1]])


def part_a():
    in_progress_paths = [(0, 0, [(0, 0)])]
    heapq.heapify(in_progress_paths)
    visited = []
    while True:
        _, curr_dist, curr_path = heapq.heappop(in_progress_paths)
        if curr_path[-1] == (pz_input.shape[0] - 1, pz_input.shape[1] - 1):
            return curr_dist
        for neighbor in [(curr_path[-1][0]-1, curr_path[-1][1]), (curr_path[-1][0]+1, curr_path[-1][1]),
                         (curr_path[-1][0], curr_path[-1][1]-1), (curr_path[-1][0], curr_path[-1][1]+1)]:
            if neighbor[0] < 0 or neighbor[0] >= pz_input.shape[0] or neighbor[1] < 0\
                    or neighbor[1] >= pz_input.shape[1] or neighbor in visited:
                continue
            new_path = curr_path.copy()
            new_path.append(neighbor)
            new_dist = curr_dist + pz_input[neighbor]
            # Dist Traveled + Estimated Heuristic (weighted Manhattan to goal), Actual Dist Traveled, Path
            heapq.heappush(in_progress_paths, (new_dist + ((pz_input.shape[0] - neighbor[0]) + (pz_input.shape[1] - neighbor[1]) * 2), new_dist, new_path))
        visited.append(curr_path[-1])


def part_b():
    global pz_input
    window = pz_input.copy()
    for _ in range(1, 5):
        new_frame = pz_input[-window.shape[0]:, -window.shape[1]:].copy()
        new_frame += 1
        new_frame[new_frame == 10] = 1
        pz_input = np.hstack((pz_input, new_frame))
    window = pz_input.copy()
    for _ in range(1, 5):
        new_frame = pz_input[-window.shape[0]:, -window.shape[1]:].copy()
        new_frame += 1
        new_frame[new_frame == 10] = 1
        pz_input = np.vstack((pz_input, new_frame))
    in_progress_paths = [(0, 0, [(0, 0)])]
    heapq.heapify(in_progress_paths)
    visited = []
    min_dist = np.inf
    while len(in_progress_paths) > 0:
        _, curr_dist, curr_path = heapq.heappop(in_progress_paths)
        if curr_path[-1] == (pz_input.shape[0] - 1, pz_input.shape[1] - 1):
            min_dist = min(min_dist, curr_dist)
            continue
        if curr_dist >= min_dist:
            continue
        for neighbor in [(curr_path[-1][0] - 1, curr_path[-1][1]), (curr_path[-1][0] + 1, curr_path[-1][1]),
                         (curr_path[-1][0], curr_path[-1][1] - 1), (curr_path[-1][0], curr_path[-1][1] + 1)]:
            if neighbor[0] < 0 or neighbor[0] >= pz_input.shape[0] or neighbor[1] < 0 \
                    or neighbor[1] >= pz_input.shape[1] or neighbor in visited:
                continue
            new_path = curr_path.copy()
            new_path.append(neighbor)
            new_dist = curr_dist + pz_input[neighbor]
            # Dist Traveled + Estimated Heuristic (weighted Manhattan to goal), Actual Dist Traveled, Path
            heapq.heappush(in_progress_paths, (new_dist + (((pz_input.shape[0] - neighbor[0]) + (pz_input.shape[1] - neighbor[1])) * 2), new_dist, new_path))
        visited.append(curr_path[-1])
    return min_dist


if __name__ == "__main__":
    # print("Part A", part_a())
    print("Part B", part_b())
