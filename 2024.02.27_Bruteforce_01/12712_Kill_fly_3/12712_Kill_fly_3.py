import sys
sys.stdin = open('in1.txt')

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
ei = [1, 1, -1, -1]
ej = [1, -1, 1, -1]

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    kill_max = []
    kill__max = []

    for r in range(N):
        for c in range(N):
            kill = arr[r][c]
            kill_ = arr[r][c]
            for m in range(1, M):
                for i in range(4):
                    ni = r + di[i] * m
                    nj = c + dj[i] * m
                    mi = r + ei[i] * m
                    mj = c + ej[i] * m
                    if 0 <= ni < N and 0 <= nj < N:
                        kill += arr[ni][nj]

                    if 0 <= mi < N and 0 <= mj < N:
                        kill_ += arr[mi][mj]

            kill_max.append(kill)
            kill__max.append(kill_)

    ans = max(kill_max)
    if ans < max(kill__max):
        ans = max(kill__max)

    print(f'#{t} {ans}')