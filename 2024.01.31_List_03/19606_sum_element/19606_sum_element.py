import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = []

    for n in range(N):
        r = list(map(int, input().split()))
        arr.append(r)

    sum_arr = 0
    for i in range(5):
        sum_arr += arr[i][i]
        sum_arr += arr[i][4 - i]
    sum_arr -= arr[2][2]

    print(f'#{t} {sum_arr}')