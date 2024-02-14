import sys
sys.stdin = open('4881_input.txt')

def arr_min_sum(i, N, s):
    global min_v
    if s >= min_v:
        return
    if i == N:
        if min_v > s:
            min_v = s
    else:
        for j in range(i, N):
            a[i], a[j] = a[j], a[i]
            arr_min_sum(i + 1, N, s + arr[i][a[i]])
            a[i], a[j] = a[j], a[i]

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    a = [i for i in range(N)]
    min_v = 100
    arr_min_sum(0, N, 0)

    print(f'#{t} {min_v}')