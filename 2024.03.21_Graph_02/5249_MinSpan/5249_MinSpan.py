import sys
sys.stdin = open('5249_input.txt')
from heapq import heappop, heappush

def prim(start):
    pq = []
    mst = [0] * (V + 1)
    sum_weight = 0
    heappush(pq, (0, start))
    while pq:
        weight, now = heappop(pq)
        if mst[now]:
            continue
        mst[now] = 1
        sum_weight += weight
        for to in graph[now]:
            heappush(pq, (to[0], to[1]))
    return sum_weight

T =int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([w, e])
        graph[e].append(([w, s]))
    ans = prim(0)
    print(f'#{t} {ans}')