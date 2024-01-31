import sys
sys.stdin = open('4837_input.txt')

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())

def sum_set(arr, n, N, K):
    list_lsit = []
    for i in range(1 << n):
        s = 0
        list_set = []
        for j in range(n):
            if i & (1 << j):
                s += arr[j]
                list_set.append(arr[j])
        if s == K:
            if len(list_set) == N:
                list_lsit.append(list_set)
    return len(list_lsit)

for t in range(1, T + 1):
    N, K = map(int, input().split())
    a = sum_set(A, 12, N, K)
    print(f'#{t} {a}')