import sys
sys.stdin = open('5248_input.txt')

def make_group(n):
    stack = [n]
    group = [n]
    while stack:
        num = stack.pop()
        for i in relation[num]:
            if i in group:
                continue
            group.append(i)
            stack.append(i)
    group.sort()
    if group not in groups:
        groups.append(group)
    return


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    relation = [[] for _ in range(N + 1)]
    for i in range(M):
        relation[arr[2 * i]].append(arr[2 * i + 1])
        relation[arr[2 * i + 1]].append(arr[2 * i])
    groups = []
    for m in range(1, N + 1):
        make_group(m)
    ans = len(groups)
    print(relation)
    print(groups)
    print(f'#{t} {ans}')