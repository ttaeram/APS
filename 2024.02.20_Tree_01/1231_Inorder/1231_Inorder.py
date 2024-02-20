import sys
sys.stdin = open('input.txt')

def in_order(T):
    if T:
        in_order(left[T])
        ans.append(arr[T])
        in_order(right[T])

T = 10
for t in range(1, T + 1):
    N = int(input())
    arr = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    par = [0] * (N + 1)

    for n in range(N):
        com = input().split()
        idx = int(com[0])
        word = com[1]
        arr[idx] = word

        if len(com) == 3:
            left[idx] = int(com[2])
            par[int(com[2])] = idx

        elif len(com) == 4:
            left[idx] = int(com[2])
            par[int(com[2])] = idx
            right[idx] = int(com[3])
            par[int(com[3])] = idx

    c = N
    while par[c] != 0:
        c = par[c]
    root = c
    ans = []
    in_order(root)
    print(f'#{t}', ''.join(ans))