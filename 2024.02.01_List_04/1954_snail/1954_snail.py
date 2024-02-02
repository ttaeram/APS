import sys
sys.stdin = open('input.txt')

T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for t in range(1, T + 1):
    N = int(input())
    arr = [([0] * N) for _ in range(N)]
    num = 0
    idx = 0
    while num <= N ** 2:
        num += 1
        if num <= N:
            arr[0][idx] = num
            idx += 1
    # for i in range(N):
    #     for j in range(N):
    #         num += 1
    #         if i == 0:
    #             arr[i][j] = num
    #         elif i == 1 and j == N-1:
    #             arr[i][j] = N + 1
    #         else:
    #             for k in range(4):
    #                 ni = i + di[k]
    #                 nj = i + dj[k]
    #                 if 0 <= ni < N and 0 <= nj < N:
    #                     if arr[ni][nj] == 0:
    #                         arr[ni][nj] = num

    print(arr)