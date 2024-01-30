import sys
sys.stdin = open('4828_input.txt')

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_a = 0
    min_a = 100000000
    dif = 0

    for j in arr:
        if j > max_a:
            max_a = j
        if j < min_a:
            min_a = j
        dif = max_a - min_a

    print(f'#{i} {dif}')
