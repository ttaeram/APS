import sys
sys.stdin = open('input.txt')

tc = 10
for i in range(1, tc + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    total_h = 0

    for n in range(2, N - 2):
        max_h = 0
        min_h = 100000000
        arr_5 = [arr[n] - arr[n - 1], arr[n] - arr[n - 2], arr[n] - arr[n + 1], arr[n] - arr[n + 2]]
        for j in arr_5:
            if j < min_h:
                min_h = j
        if min_h > 0:
            total_h += min_h
    print(f'#{i} {total_h}')
    #     for j in range(4):
    #         max_h = arr_5[0]
    #         if max_h < arr_5[j]:
    #             max_h = arr_5[j]
    #     arr_5.remove(max_h)
    #     for j in range(3):
    #         sec_h = arr_5[0]
    #         if sec_h < arr_5[j]:
    #             sec_h = arr_5[j]
    #     h_dif = max_h - sec_h
    #     if h_dif > 0:
    #         total_h += h_dif
    #     else:
    #         continue
    # print(total_h)