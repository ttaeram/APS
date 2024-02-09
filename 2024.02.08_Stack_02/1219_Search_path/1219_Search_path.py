import sys
sys.stdin = open('input.txt')

T = 10

def DFS(i):
    stack = []
    visited[i] = 1
    result.append(i)
    while True:
        for w in adj_list[i]:
            if visited[w] == 0:
                stack.append(i)
                i = w
                visited[i] = 1
                result.append(i)
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break
    return result

for t in range(1, T + 1):
    N, E = map(int, input().split())
    arr = list(map(int, input().split()))
    adj_list = [[] for _ in range(100)]
    result = []

    for i in range(E):
        start, end = arr[i * 2], arr[i * 2 + 1]
        adj_list[start].append(end)

    visited = [0] * 100
    DFS(0)

    if 99 in result:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')

