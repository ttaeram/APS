import sys
sys.stdin = open('input.txt')

def bfs(num):
    queue = [num]
    visited[num] = 1

    while queue:
        n = queue.pop(0)
        ans.append(n)

        for l in path[n]:
            if visited[l] == 1:
                continue
            visited[l] = 1
            queue.append(l)

t = 1
V, E = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * (V + 1)
path = [[] for _ in range(V + 1)]
for i in range(E):
    path[arr[2 * i]].append(arr[2 * i + 1])
ans = []
bfs(1)
print(f'#{t}', *ans)