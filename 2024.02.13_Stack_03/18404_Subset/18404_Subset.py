import sys
sys.stdin = open('input.txt')

T = 1
arr = list(map(int, input().split()))

n = len(arr)

cnt = 0
for i in range(1 << n):
    arr_s = []
    for j in range(n):
        if i & (1 << j):
            arr_s.append(arr[j])
    if sum(arr_s) == 10:
        cnt += 1

print(f'#{T} {cnt}')