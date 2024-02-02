import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = 0
    min_v = 11
    max_idx = -1
    min_idx = 100
    for idx in range(N):
        if arr[idx] >= max_v:
            max_v = arr[idx]
            max_idx = idx

    for idxs in range(N):
        if arr[idxs] < min_v:
            min_v = arr[idxs]
            min_idx = idxs

    gap = abs(max_idx - min_idx)
    print(f'#{t} {gap}')