import sys
sys.stdin = open('5189_input.txt')

def search(x):
    global min_sum
    s = 0
    if x == N:
        new_path = path + [0]
        for j in range(len(path)):
            s += arr[new_path[j]][new_path[j + 1]]
        if min_sum > s:
            min_sum = s
        return

    for i in range(1, N):
        if used[i]:
            continue
        used[i] = True
        path.append(i)
        search(x + 1)
        path.pop()
        used[i] = False

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    path = [0]
    used = [False] * N
    min_sum = 100000000

    search(1)
    print(f'#{t} {min_sum}')