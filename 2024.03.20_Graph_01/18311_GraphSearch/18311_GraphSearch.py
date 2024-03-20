import sys
sys.stdin = open('input.txt')

def dfs(i):
    if i == 1:
        print(i, end = '')
        visited[i] = 1
    else:
        print(f'-{i}', end='')
    for l in path[i]:
        if visited[l] == 1:
            continue

        visited[l] = 1
        dfs(l)
t = 1
V, E = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * (V + 1)
path = [[] for _ in range(V + 1)]
for i in range(E):
    path[arr[2 * i]].append(arr[2 * i + 1])
    path[arr[2 * i + 1]].append(arr[2 * i])

print('#1', end = ' ')
dfs(1)