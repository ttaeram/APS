import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())    # 달팽이 크기

    # 달팽이를 그리기 위해 리스트를 미리 준비
    snail = [[0] * N for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    direct = 0

    row = 0
    col = 0
    num = 1
    snail[row][col] = num
    while num < N *N:   # 채워지는 숫자만큰 반복
        # 이동할 위치가 달팽이 범위 내에 있는지 확인
        # for _ in range(4):  # 특정 조건에서 방향을 전환해야 하기 때문에 사용하지 않음
        nr = row + dr[direct]
        nc = col + dc[direct]

        if 0 <= nr < N and 0 <= nc < N and snail[nr][nc] == 0:
            # 이동하려는 방향이 범위 내인지 확인
            # 값이 비어있는지 확인
            # if snail[nr][nc] == 0:
                num += 1
                row = nr
                col = nc
                snail[row][col] = num
            # else:
            #     direct = (direct + 1) % 4   # 방향 범위를 맞추기 위함
        else:
            direct = (direct + 1) % 4

    print(f'#{t}')
    for row in range(N):
        print(*snail[row])
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# for t in range(1, T + 1):
#     N = int(input())
#     arr = [([0] * N) for _ in range(N)]
#     num = 0
#     idx = 0
#     while num <= N ** 2:
#         num += 1
#         if num <= N:
#             arr[0][idx] = num
#             idx += 1
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