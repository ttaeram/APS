import sys
sys.stdin = open('5178_input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    heap = [0] * (N + 1)

    for m in range(M):
        leaf, value = map(int, input().split())
        heap[leaf] = value

    if N % 2 == 1:
        i = N - 1
    else:
        i = N

    while i > 0:
        if i == N:
            heap[i // 2] = heap[i]
        else:
            heap[i // 2] = heap[i] + heap[i + 1]
        i -= 2

    ans = heap[L]
    print(f'#{t} {ans}')