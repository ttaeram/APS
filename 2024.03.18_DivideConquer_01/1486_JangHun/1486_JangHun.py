import sys
sys.stdin = open('input.txt')

def comb(n):
    global ans
    if n == N:
        res = 0
        for i in range(N):
            if check[i] == 1:
                res += arr[i]
        if res == B:
            ans = 0
            return
        elif res > B:
            ans = min(res - B, ans)
            return
        else:
            return
    check[n] = 1
    comb(n + 1)
    check[n] = 0
    comb(n + 1)

T = int(input())
for t in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    check = [0] * N
    ans = float("inf")
    comb(0)

    print(f'#{t} {ans}')

