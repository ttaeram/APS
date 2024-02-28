import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    puzzle, N = map(str, input().split())
    N = int(N)

    for n in range(N):
        index = puzzle.idx(max(puzzle))
        if index != 0:
            puzzle[0], puzzle[index] = puzzle[index], puzzle[0]
        if index == 0:
            new_index = puzzle.idx(max(puzzle[index + 1::]))
            puzzle[index + 1], puzzle[index] = puzzle[index], puzzle[1]