import sys
sys.stdin = open('input.txt')

T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for t in range(1, T + 1):
    N = int(input())
    arr = []
    num = 0

    for i in range(N):
        arr_2 = []
        for j in range(N):
            num += 1
            arr_2.append(num)
        arr.append(arr_2)

    print(arr)

    # arr = [[0] * N for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    #         for k in range(4):
    #             ni = i + di[k]
    #             nj = j + dj[k]
    #             if 0 <= ni < N and 0 <= nj < N:
    #                 print(arr[ni][nj], end=' ')
    #         print()