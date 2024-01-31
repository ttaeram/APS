import sys
sys.stdin = open('input.txt')

T = int(input())
N = 10

def set_sum(arr, N):
    for i in range(1, 1 << N):
        s = 0
        for j in range(N):
            if i & (1 << j):
                s += arr[j]
        if s == 0:
            return 1
    return 0

for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    result = set_sum(arr, N)
    print(f'#{t} {result}')