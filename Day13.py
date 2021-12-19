from PuzzleInput import ReadInput
import numpy as np

pz_input = ReadInput(13).data
print(pz_input)
# pz_input = ['6,10',
#             '0,14',
#             '9,10',
#             '0,3',
#             '10,4',
#             '4,11',
#             '6,0',
#             '6,12',
#             '4,1',
#             '0,13',
#             '10,12',
#             '3,4',
#             '3,0',
#             '8,4',
#             '1,10',
#             '2,14',
#             '8,10',
#             '9,0',
#             '',
#             'fold along y=7',
#             'fold along x=5']
paper = None
folds = None


def build_map():
    global paper
    global folds
    starting_locs = []
    folds = []
    loading_locs = True
    for line in pz_input:
        if loading_locs:
            if line == "":
                loading_locs = False
                continue
            pieces = line.split(',')
            starting_locs.append((int(pieces[1]), int(pieces[0])))
        else:
            if line == "":
                continue
            pieces = line.split(' ')[-1].split('=')
            folds.append((pieces[0], int(pieces[1])))
    paper = np.zeros((max([x[0] for x in starting_locs])+1, max([x[1] for x in starting_locs])+1))
    for loc in starting_locs:
        paper[loc[0], loc[1]] = 1


def fold(curr_paper, axis, index):
    curr_paper = curr_paper.astype(bool)
    if axis == 'x':
        fold_over = np.fliplr(curr_paper[:, index+1:])
        curr_paper = curr_paper[:, :index]
        curr_paper[:, -fold_over.shape[1]:] = np.logical_or(curr_paper[:, -fold_over.shape[1]:], fold_over)
        print(curr_paper.astype(int))
        return curr_paper.astype(int)
    elif axis == 'y':
        fold_over = np.flipud(curr_paper[index + 1:, :])
        curr_paper = curr_paper[:index, :]
        curr_paper[-fold_over.shape[0]:, :] = np.logical_or(curr_paper[-fold_over.shape[0]:, :], fold_over)
        print(curr_paper.astype(int))
        return curr_paper.astype(int)


def part_a():
    global paper
    global folds
    if paper is None:
        build_map()
    paper_a = paper.copy()
    first_fold = folds[0]
    return np.sum(fold(paper_a, first_fold[0], first_fold[1]))


def part_b():
    global paper
    global folds
    if paper is None:
        build_map()
    paper_b = paper.copy()
    for curr_fold in folds:
        paper_b = fold(paper_b, curr_fold[0], curr_fold[1])
    np.set_printoptions(edgeitems=30, linewidth=100000,
                        formatter=dict(float=lambda x: "%.3g" % x))
    for row in paper_b:
        print(['#' if x == 1 else '.' for x in row])


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
