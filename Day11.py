from PuzzleInput import ReadInput
import numpy as np

pz_input = np.array([[int(y) for y in x] for x in ReadInput(11).data if x != ""])
print(pz_input)
# pz_input = np.array([[int(y) for y in x] for x in ['5483143223',
#                                                    '2745854711',
#                                                    '5264556173',
#                                                    '6141336146',
#                                                    '6357385478',
#                                                    '4167524645',
#                                                    '2176841721',
#                                                    '6882881134',
#                                                    '4846848554',
#                                                    '5283751526']])


def part_a():
    oct_a = pz_input.copy()
    flashes = 0
    for _ in range(100):
        oct_a += 1
        to_flash = [(x[0], x[1]) for x in np.argwhere(oct_a > 9)]
        flashed = []
        while len(to_flash) > 0:
            row, col = to_flash.pop()
            flashed.append((row, col))
            oct_a[max(0, row-1):row+2, max(0, col-1):col+2] += 1
            flashes += 1
            new_flashes = [(x[0], x[1]) for x in np.argwhere(oct_a > 9) if (x[0], x[1]) not in to_flash and (x[0], x[1]) not in flashed]
            if len(new_flashes) > 0:
                to_flash.extend(new_flashes)
        oct_a[oct_a > 9] = 0
    return flashes


def part_b():
    oct_b = pz_input.copy()
    flashes = 0
    i = 0
    while True:
        i += 1
        oct_b += 1
        to_flash = [(x[0], x[1]) for x in np.argwhere(oct_b > 9)]
        flashed = []
        while len(to_flash) > 0:
            row, col = to_flash.pop()
            flashed.append((row, col))
            oct_b[max(0, row - 1):row + 2, max(0, col - 1):col + 2] += 1
            flashes += 1
            new_flashes = [(x[0], x[1]) for x in np.argwhere(oct_b > 9) if
                           (x[0], x[1]) not in to_flash and (x[0], x[1]) not in flashed]
            if len(new_flashes) > 0:
                to_flash.extend(new_flashes)
        oct_b[oct_b > 9] = 0
        if np.sum(oct_b) == 0:
            return i


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
