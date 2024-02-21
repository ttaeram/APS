import sys
sys.stdin = open('5177_input.txt')

def min_heap(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p >= 1 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0] * (N + 1)
    last = 0

    for i in arr:
        min_heap(i)

    idx = N
    res = 0
    while idx > 1:
        idx = idx // 2
        res += heap[idx]

    print(f'#{t} {res}')