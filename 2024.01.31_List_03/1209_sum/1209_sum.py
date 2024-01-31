import sys
sys.stdin = open('1209_sum_input.txt')

T = 10
for t in range(1, T + 1):
    N = int(input())
    # arr = [list(map(int, input().split())) for i in range(100)]
    arr = []
    for i in range(100):
        n = list(map(int, input().split()))
        arr.append(n)

    list_max = []

    max_c = 0
    for r in range(100):
        sum_c = 0
        for c in range(100):
            sum_c += arr[r][c]
        if max_c < sum_c:
            max_c = sum_c
    list_max.append(max_c)

    max_r = 0
    for c in range(100):
        sum_r = 0
        for r in range(100):
            sum_r += arr[r][c]
        if max_r < sum_r:
            max_r = sum_r
    list_max.append(max_r)

    max_rc = 0
    sum_rc = 0
    for rc in range(100):
        sum_rc += arr[rc][rc]

    for rc in range(100):
        max_rc += arr[rc][99 - rc]

    if max_rc > sum_rc:
        list_max.append(max_rc)
    elif max_rc < sum_rc:
        list_max.append(sum_rc)
    elif max_rc == sum_rc:
        list_max.append(max_rc)

    real_max = 0
    for max_ in list_max:
        if real_max < max_:
            real_max = max_

    print(f'#{t} {real_max}')