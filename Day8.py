from PuzzleInput import ReadInput
import numpy as np

pz_input = ReadInput(8).data
# pz_input = ['be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
# 'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
# 'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
# 'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
# 'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
# 'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
# 'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
# 'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
# 'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
# 'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce']
print(pz_input)
displays = [x.split(" | ") for x in pz_input if x != ""]


def part_a():
    total = 0
    for display in displays:
        total += sum([1 for x in display[1].split(" ") if len(x) in [2, 3, 4, 7]])
    return total


def part_b():
    running_total = 0
    def remove(domain, key, pos):
        try:
            domain[key].remove(pos)
        except ValueError:
            pass

    def build_converter(domain):
        inverted_domain = {}
        for k, v in domain.items():
            inverted_domain[v[0]] = k
        converter = {"".join(sorted(inverted_domain['VT'] +
                                    inverted_domain['TL'] +
                                    inverted_domain['TR'] +
                                    inverted_domain['BL'] +
                                    inverted_domain['BR'] +
                                    inverted_domain['VB'])): '0',
                     "".join(sorted(inverted_domain['TR'] +
                                    inverted_domain['BR'])): '1',
                     "".join(sorted(inverted_domain['VT'] +
                                    inverted_domain['TR'] +
                                    inverted_domain['MI'] +
                                    inverted_domain['BL'] +
                                    inverted_domain['VB'])): '2',
                     "".join(sorted(inverted_domain['VT'] +
                                    inverted_domain['TR'] +
                                    inverted_domain['MI'] +
                                    inverted_domain['BR'] +
                                    inverted_domain['VB'])): '3',
                     "".join(sorted(inverted_domain['TL'] +
                                    inverted_domain['TR'] +
                                    inverted_domain['MI'] +
                                    inverted_domain['BR'])): '4',
                     "".join(sorted(inverted_domain['VT'] +
                                    inverted_domain['TL'] +
                                    inverted_domain['MI'] +
                                    inverted_domain['BR'] +
                                    inverted_domain['VB'])): '5',
                     "".join(sorted(inverted_domain['VT'] +
                                    inverted_domain['TL'] +
                                    inverted_domain['MI'] +
                                    inverted_domain['BL'] +
                                    inverted_domain['BR'] +
                                    inverted_domain['VB'])): '6',
                     "".join(sorted(inverted_domain['VT'] +
                                    inverted_domain['TR'] +
                                    inverted_domain['BR'])): '7',
                     "".join(sorted(inverted_domain['VT'] +
                                    inverted_domain['TL'] +
                                    inverted_domain['TR'] +
                                    inverted_domain['MI'] +
                                    inverted_domain['BL'] +
                                    inverted_domain['BR'] +
                                    inverted_domain['VB'])): '8',
                     "".join(sorted(inverted_domain['VT'] +
                                    inverted_domain['TL'] +
                                    inverted_domain['TR'] +
                                    inverted_domain['MI'] +
                                    inverted_domain['BR'] +
                                    inverted_domain['VB'])): '9'}
        return converter

    for display in displays:
        samples = display[0].split(' ')
        nums = {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': ['abcdefg'], '9': []}
        for sample in samples:
            curr = "".join(sorted(sample))
            if len(curr) == 7:
                continue
            elif len(curr) == 2:
                nums['1'].append(curr)
            elif len(curr) == 3:
                nums['7'].append(curr)
            elif len(curr) == 4:
                nums['4'].append(curr)
            elif len(curr) == 5:
                nums['2'].append(curr)
                nums['3'].append(curr)
                nums['5'].append(curr)
            elif len(curr) == 6:
                nums['0'].append(curr)
                nums['6'].append(curr)
                nums['9'].append(curr)
        domain = {'a': ['VT', 'TL', 'TR', 'MI', 'BL', 'BR', 'VB'],
                  'b': ['VT', 'TL', 'TR', 'MI', 'BL', 'BR', 'VB'],
                  'c': ['VT', 'TL', 'TR', 'MI', 'BL', 'BR', 'VB'],
                  'd': ['VT', 'TL', 'TR', 'MI', 'BL', 'BR', 'VB'],
                  'e': ['VT', 'TL', 'TR', 'MI', 'BL', 'BR', 'VB'],
                  'f': ['VT', 'TL', 'TR', 'MI', 'BL', 'BR', 'VB'],
                  'g': ['VT', 'TL', 'TR', 'MI', 'BL', 'BR', 'VB']}
        for letter in 'abcdefg':
            tot = 0
            for option in samples:
                if letter in option:
                    tot += 1
            if tot == 4:
                remove(domain, letter, 'VT')
                remove(domain, letter, 'TL')
                remove(domain, letter, 'TR')
                remove(domain, letter, 'MI')
                remove(domain, letter, 'BR')
                remove(domain, letter, 'VB')
                for other in 'abcdefg':
                    if other == letter:
                        continue
                    remove(domain, other, 'BL')
            elif tot == 6:
                remove(domain, letter, 'VT')
                remove(domain, letter, 'TR')
                remove(domain, letter, 'MI')
                remove(domain, letter, 'BL')
                remove(domain, letter, 'BR')
                remove(domain, letter, 'VB')
                for other in 'abcdefg':
                    if other == letter:
                        continue
                    remove(domain, other, 'TL')
            elif tot == 9:
                remove(domain, letter, 'VT')
                remove(domain, letter, 'TR')
                remove(domain, letter, 'TL')
                remove(domain, letter, 'MI')
                remove(domain, letter, 'BL')
                remove(domain, letter, 'VB')
                for other in 'abcdefg':
                    if other == letter:
                        continue
                    remove(domain, other, 'BR')
        for letter in nums['1'][0]:
            remove(domain, letter, 'VT')
            remove(domain, letter, 'TL')
            remove(domain, letter, 'MI')
            remove(domain, letter, 'BL')
            remove(domain, letter, 'VB')
        for letter in nums['4'][0]:
            remove(domain, letter, 'VT')
            remove(domain, letter, 'BL')
            remove(domain, letter, 'VB')
        for letter in nums['7'][0]:
            remove(domain, letter, 'TL')
            remove(domain, letter, 'MI')
            remove(domain, letter, 'BL')
            remove(domain, letter, 'VB')
            if letter not in nums['1'][0]:
                remove(domain, letter, 'TR')
                remove(domain, letter, 'BR')
                for other in 'abcdefg':
                    if other == letter:
                        continue
                    remove(domain, other, 'VT')
        for poss in nums['9']:
            extras = [x for x in poss if x not in nums['4'][0] + [y for y in domain if 'VT' in domain[y]][0]]
            if len(extras) == 1:
                remove(domain, extras[0], 'VT')
                remove(domain, extras[0], 'TL')
                remove(domain, extras[0], 'TR')
                remove(domain, extras[0], 'MI')
                remove(domain, extras[0], 'BL')
                remove(domain, extras[0], 'BR')
                for other in 'abcdefg':
                    if other == extras[0]:
                        continue
                    remove(domain, other, 'VB')
                break
        for key in domain:
            if len(domain[key]) == 1:
                for other in 'abcdefg':
                    if other == key:
                        continue
                    remove(domain, other, domain[key][0])
        digit_converter = build_converter(domain)
        running_total += int("".join([digit_converter["".join(sorted(x))] for x in display[1].split(' ')]))
    return running_total


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
