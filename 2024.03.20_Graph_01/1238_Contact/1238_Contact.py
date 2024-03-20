import sys
sys.stdin = open('input.txt')

def calling(S):
    stack = [(S, 0)]
    res.append((S, 0))

    while stack:
        s = stack.pop(0)
        for m in friend[s[0]]:
            if visited[m] == 1:
                continue
            visited[m] = 1
            stack.append((m, s[1] + 1))
            res.append((m, s[1] + 1))
            priority.add(s[1] + 1)

T = 10
for t in range(1, T + 1):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    friend = [[] for _ in range(101)]
    for i in range(N // 2):
        friend[arr[2 * i]].append(arr[2 * i + 1])
    visited = [0] * 101
    res = []
    priority = set()
    calling(S)
    ans_priority = max(priority)
    ans = 0
    for r in res:
        if r[1] == ans_priority:
            ans = max(ans, r[0])
    print(f'#{t} {ans}')
