from PuzzleInput import ReadInput
import numpy as np

pz_input = [x.split(" ") for x in ReadInput(2).data if x != ""]
print(pz_input)


def part_a():
    loc = [0, 0]
    for command, amount in pz_input:
        if command == "forward":
            loc[0] += int(amount)
        elif command == "down":
            loc[1] += int(amount)
        elif command == "up":
            loc[1] -= int(amount)
    return loc[0] * loc[1]


def part_b():
    loc = [0, 0, 0]
    for command, amount in pz_input:
        if command == "forward":
            loc[0] += int(amount)
            loc[1] += int(amount) * loc[2]
        elif command == "down":
            loc[2] += int(amount)
        elif command == "up":
            loc[2] -= int(amount)
    return loc[0] * loc[1]


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
