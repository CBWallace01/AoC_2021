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
    # VT: Very Top, TL: Top Left, TR: Top Right, MI: Middle, BL: Bottom Left, BR: Bottom Right, VB: Very Bottom
    start_domains = {'a': ['VT', 'TL', 'TR', 'MI', 'BL', 'BR', 'VB'],
                     'b': ['VT', 'TL', 'TR', 'MI', 'BL', 'BR', 'VB'],
                     'c': ['VT', 'TL', 'TR', 'MI', 'BL', 'BR', 'VB'],
                     'd': ['VT', 'TL', 'TR', 'MI', 'BL', 'BR', 'VB'],
                     'e': ['VT', 'TL', 'TR', 'MI', 'BL', 'BR', 'VB'],
                     'f': ['VT', 'TL', 'TR', 'MI', 'BL', 'BR', 'VB'],
                     'g': ['VT', 'TL', 'TR', 'MI', 'BL', 'BR', 'VB']}

    def validate_domain(domain):
        for key in domain.keys():
            if len(domain[key]) > 1:
                return False
        return True

    def remove(domain, key, pos):
        try:
            domain[key].remove(pos)
        except ValueError:
            pass

    for display in displays:
        curr_domain = start_domains.copy()
        samples = display[0].split(' ')
        idx = 0
        while idx < len(samples):  # not validate_domain(curr_domain):
            curr = samples[idx]
            # 8 - No usable information here or if all letters are solved
            if len(curr) == 7 or sum([len(curr_domain[x]) for x in curr]) > len(curr):
                pass
            # 1
            elif len(curr) == 2:
                for letter in curr:
                    remove(curr_domain, letter, 'VT')
                    remove(curr_domain, letter, 'TL')
                    remove(curr_domain, letter, 'BL')
                    remove(curr_domain, letter, 'MI')
                    remove(curr_domain, letter, 'VB')
            # 7
            elif len(curr) == 3:
                for letter in curr:
                    remove(curr_domain, letter, 'TL')
                    remove(curr_domain, letter, 'BL')
                    remove(curr_domain, letter, 'MI')
                    remove(curr_domain, letter, 'VB')
            # 4
            elif len(curr) == 4:
                for letter in curr:
                    remove(curr_domain, letter, 'VT')
                    remove(curr_domain, letter, 'BL')
                    remove(curr_domain, letter, 'VB')
            # 2 / 3 / 5
            elif len(curr) == 5:
                pass
            # 0 / 6 / 9
            elif len(curr) == 6:
                pass
            idx += 1
        debug = True


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
