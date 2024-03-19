import sys
sys.stdin = open('5209_input.txt')

def comb(num, res):
    global ans
    if ans < res:
        return

    if num == N:
        ans = res
        return

    for i in range(num, N):
        idx[num], idx[i] = idx[i], idx[num]
        comb(num + 1, res + arr[num][idx[num]])
        idx[num], idx[i] = idx[i], idx[num]

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    idx = [j for j in range(N)]
    ans = 15000
    comb(0, 0)
    print(f'#{t} {ans}')