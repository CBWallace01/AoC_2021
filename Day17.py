from PuzzleInput import ReadInput
import numpy as np

pz_input = ReadInput(17).data[0]
print(pz_input)
# pz_input = 'target area: x=20..30, y=-10..-5'
x = []
y = []


def parse_input():
    global x, y
    pieces = pz_input.split(' ')
    x = [int(x) for x in pieces[2][2:-1].split('..')]
    y = [int(y) for y in pieces[3][2:].split('..')]


def take_shot(x_vel, y_vel):
    x_pos = 0
    y_pos = 0
    max_height = None
    while True:
        if y_vel == 0:
            max_height = y_pos
        x_pos += x_vel
        y_pos += y_vel
        x_vel = max(0, x_vel - 1)
        y_vel -= 1
        if x[0] <= x_pos <= x[1] and y[0] <= y_pos <= y[1]:
            return 0, max_height
        elif x_pos < x[0] and y_pos < y[0]:
            # Fell Short
            return -1, None
        elif x_pos > x[1]:
            # Over Shot
            return -2, None
        elif x[0] <= x_pos <= x[1] and y_pos < y[0]:
            # Fell through too fast
            return -3, None


def part_a():
    global x, y
    if len(x) == 0 or len(y) == 0:
        parse_input()
    x_tot = 0
    x_vel_range = []
    for i in range(x[1]):
        x_tot += i
        if x[0] <= x_tot <= x[1] and len(x_vel_range) == 0:
            x_vel_range.append(i)
        elif x_tot > x[1]:
            x_vel_range.append(i)
            break
    max_height = 0
    for x_vel in range(x_vel_range[0], x_vel_range[1]+1):
        for y_vel in range(abs(y[1]), abs(y[0]) + 1):
            result, height = take_shot(x_vel, y_vel)
            if result == 0:
                max_height = max(height, max_height)
    return max_height


def part_b():
    global x, y
    if len(x) == 0 or len(y) == 0:
        parse_input()
    valid_count = 0
    for x_vel in range(x[1] + 1):
        for y_vel in range(y[0], abs(y[0]) + 1):
            result, height = take_shot(x_vel, y_vel)
            if result == 0:
                valid_count += 1
    return valid_count


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
