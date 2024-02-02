import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    carrot = list(map(int, input().split()))
    max_grow = 0
    grow_cnt = 1

    for n in range(1, N):
        if carrot[n] > carrot[n - 1]:
            grow_cnt += 1

        elif carrot[n] < carrot[n - 1]:
            grow_cnt = 1

        if max_grow < grow_cnt:
            max_grow = grow_cnt

    print(f'#{t} {max_grow}')