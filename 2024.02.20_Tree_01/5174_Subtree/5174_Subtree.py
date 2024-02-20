import sys
sys.stdin = open('5174_input.txt')

def pre_order(T):
    if T:
        res.append(T)
        pre_order(left[T])
        pre_order(right[T])

T = int(input())
for t in range(1, T + 1):
    E, target = map(int, input().split())
    arr = list(map(int, input().split()))
    N = E + 1
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    par = [0] * (N + 1)
    res = []

    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        par[c] = p

    pre_order(target)
    ans = len(res)
    print(f'#{t} {ans}')