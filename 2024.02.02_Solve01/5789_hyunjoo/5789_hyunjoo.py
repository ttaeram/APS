import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T + 1):
    N, Q = map(int, input().split())
    arr = [0] * N
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L, R + 1):
            arr[j-1] = i

    print(f'#{t}', *arr)