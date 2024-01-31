import sys
sys.stdin = open('4836_input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    purple = 3
    purple_cnt = 0
    board = [[0] * 10 for _ in range(10)]

    for n in range(N):
        setting = list(map(int, input().split()))
        for i in range(setting[0], setting[2] + 1):
            for j in range(setting[1], setting[3] + 1):
                board[i][j] += setting[4]

    for r in range(10):
        for c in range(10):
            if board[r][c] == purple:
                purple_cnt += 1
    print(f'#{t} {purple_cnt}')