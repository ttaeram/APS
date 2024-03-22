import sys
sys.stdin = open('5251_input.txt')
from heapq import heappush, heappop

def dijkstra(start):
    pq = []
    heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        dist, now = heappop(pq)
        # if distance[now] < dist:
        #     continue

        for to in graph[now]:
            n_dist = to[0]
            n_node = to[1]
            new_dist = dist + n_dist
            if new_dist >= distance[n_node]:
                continue
            distance[n_node] = new_dist
            heappush(pq, (new_dist, n_node))

T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([w, e])
    start = 0
    inf = int(1e9)
    distance = [inf] * (N + 1)
    dijkstra(0)
    ans = distance[N]
    print(graph)
    print(distance)
    print(f'#{t} {ans}')