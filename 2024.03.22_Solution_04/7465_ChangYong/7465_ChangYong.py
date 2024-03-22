import sys
sys.stdin = open('s_input.txt')

def make_group(n):
    stack = [n]
    group = [n]
    while stack:
        num = stack.pop()
        visit[num] = 1
        for i in relation[num]:
            if i in group:
                continue
            group.append(i)
            stack.append(i)
    groups.add(tuple(group))
    return

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    relation = [[] for _ in range(N + 1)]
    visit = [0] * (N + 1)
    groups = set()
    for _ in range(M):
        a, b = map(int, input().split())
        relation[a].append(b)
        relation[b].append(a)

    for i in range(1, N + 1):
        if visit[i] == 0:
            make_group(i)

    ans = len(groups)
    print(f'#{t} {ans}')