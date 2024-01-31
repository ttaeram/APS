import sys
sys.stdin = open('ex1_input.txt')

di = [0, 1, 0, -1]  # 방향별로 더할 값
dj = [1, 0, -1, 0]

T = int(input())

for t in range(1, T + 1):
    arr = []
    N = int(input())

    for n in range(N):
        element = list(map(int, input().split()))
        arr.append(element)

    sum_num = 0
    dif_list = []
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    dif = abs(arr[i][j] - arr[ni][nj])
                    dif_list.append(dif)
    for difs in dif_list:
        sum_num += difs
    print(f'#{t} {sum_num}')
# di = [0, 1, 0, -1]  # 방향별로 더할 값
# dj = [1, 0, -1, 0]
# N = 5
# arr = [[0] * N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0 <= ni < N and 0 <= nj < N:
#                 print(arr[ni][nj], end = ' ')
#         print()