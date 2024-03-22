import sys
sys.stdin = open('input.txt')
from heapq import heappop, heappush

def dijkstra(start):
    distance = [int(1e9)] * (N + 1)
    pq = []
    heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        dist, now = heappop(pq)
        # if distance[now] != 0:
        #     continue
        for to in roads[now]:
            n_dist = to[0]
            n_node = to[1]
            new_dist = dist + n_dist
            if new_dist >= distance[n_node]:
                continue
            distance[n_node] = new_dist
            heappush(pq, (new_dist, n_node))
    return distance

T = int(input())
for t in range(1, T + 1):
    N, M, X = map(int, input().split())
    roads = [[] for _ in range(N + 1)]
    distance = [int(1e9)] * (N + 1)
    for _ in range(M):
        x, y, c = map(int, input().split())
        roads[x].append([c, y])
    max_ans = 0
    distance_x = dijkstra(X)
    for idx in range(1, N + 1):
        ans = 0
        distance = dijkstra(idx)
        ans += distance[X]
        ans += distance_x[idx]
        max_ans = max(ans, max_ans)

    print(f'#{t} {max_ans}')