import sys
sys.stdin = open('5201_input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    Wi = list(map(int, input().split()))
    Ti = list(map(int, input().split()))
    Wi.sort(key=None, reverse=True)
    Ti.sort(key = None, reverse = True)

    total = 0
    for ti in Ti:
        mine = 0
        for wi in range(len(Wi)):
            if Wi[wi] <= ti and Wi[wi] != 0:
                mine = Wi[wi]
                Wi[wi] = 0
                break
        total += mine

    print(f'#{t} {total}')
