from PuzzleInput import ReadInput
import numpy as np
from collections import defaultdict

pz_input = ReadInput(14).data
print(pz_input)
# pz_input = ['NNCB',
#             '',
#             'CH -> B',
#             'HH -> N',
#             'CB -> H',
#             'NH -> C',
#             'HB -> C',
#             'HC -> B',
#             'HN -> C',
#             'NN -> C',
#             'BH -> H',
#             'NC -> B',
#             'NB -> B',
#             'BN -> B',
#             'BB -> N',
#             'BC -> B',
#             'CC -> N',
#             'CN -> C']
rules = {}
elements = set([])
for i in range(2, len(pz_input)):
    if pz_input[i] == '':
        continue
    pieces = pz_input[i].split(" -> ")
    rules[pieces[0]] = pieces[1]
    elements.add(pieces[0][1])
    elements.add(pieces[0][1])
    elements.add(pieces[1])


def part_a():
    counts = defaultdict(int)
    polymer = pz_input[0]
    for i in range(len(polymer) - 1):
        counts[polymer[i] + polymer[i + 1]] += 1
    for _ in range(10):
        new_counts = defaultdict(int)
        for pair in counts:
            new_counts[pair[0] + rules[pair]] += counts[pair]
            new_counts[rules[pair] + pair[1]] += counts[pair]
        counts = new_counts
    max_element = 0
    min_element = np.inf
    for elem in elements:
        count = sum([counts[x] for x in counts if elem in x[0]])
        if elem == pz_input[0][-1]:
            count += 1
        max_element = max(max_element, count)
        min_element = min(min_element, count)
    return max_element - min_element


def part_b():
    counts = defaultdict(int)
    polymer = pz_input[0]
    for i in range(len(polymer)-1):
        counts[polymer[i]+polymer[i+1]] += 1
    for _ in range(40):
        new_counts = defaultdict(int)
        for pair in counts:
            new_counts[pair[0]+rules[pair]] += counts[pair]
            new_counts[rules[pair]+pair[1]] += counts[pair]
        counts = new_counts
    max_element = 0
    min_element = np.inf
    for elem in elements:
        count = sum([counts[x] for x in counts if elem in x[0]])
        if elem == pz_input[0][-1]:
            count += 1
        max_element = max(max_element, count)
        min_element = min(min_element, count)
    return max_element - min_element


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
