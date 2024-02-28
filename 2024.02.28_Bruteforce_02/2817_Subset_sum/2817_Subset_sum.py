import sys
sys.stdin = open('sample_input.txt')

def subset_sum(tar):
    s = 0
    for i in range(N):
        if tar & 0x1:
            s += arr[i]
        tar >>= 1
    return s

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0

    for tar in range(1 << N):
        res = subset_sum(tar)
        if res == K:
            cnt += 1
    print(f'#{t} {cnt}')
