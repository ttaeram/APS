import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_n = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            for m in range(0, M):
                for n in range(0, M):
                    kill += arr[i + m][j + n]
            if max_n < kill:
                max_n = kill

    print(f'#{t} {max_n}')