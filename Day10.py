from PuzzleInput import ReadInput
import numpy as np

pz_input = ReadInput(10).data
print(pz_input)
# pz_input = ['[({(<(())[]>[[{[]{<()<>>',
# '[(()[<>])]({[<{<<[]>>(',
# '{([(<{}[<>[]}>{[]{[(<()>',
# '(((({<>}<{<{<>}{[]{[]{}',
# '[[<[([]))<([[{}[[()]]]',
# '[{[{({}]{}}([{[{{{}}([]',
# '{<[[]]>}<{[{[{[]{()[[[]',
# '[<(<(<(<{}))><([]([]()',
# '<{([([[(<>()){}]>(<<{{',
# '<{([{{}}[<[[[<>{}]]]>[]]']
openings = '([{<'
closings = ')]}>'
error_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
incomplete_scores = {')': 1, ']': 2, '}': 3, '>': 4}


def part_a():
    total_score = 0
    for line in pz_input:
        symbols = []
        for char in line:
            if char in openings:
                symbols.append(char)
            elif char in closings:
                if symbols[-1] == openings[closings.find(char)]:
                    symbols.pop(-1)
                else:
                    total_score += error_scores[char]
                    break
    return total_score


def part_b():
    total_scores = []
    for line in pz_input:
        symbols = []
        is_incomplete = True
        for char in line:
            if char in openings:
                symbols.append(char)
            elif char in closings:
                if symbols[-1] == openings[closings.find(char)]:
                    symbols.pop(-1)
                else:
                    is_incomplete = False
                    break
        curr_score = 0
        if is_incomplete and len(symbols) > 0:
            for i in range(len(symbols)-1, -1, -1):
                curr_score *= 5
                curr_score += incomplete_scores[closings[openings.find(symbols[i])]]
            total_scores.append(curr_score)
    total_scores.sort()
    return total_scores[len(total_scores) // 2]


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
