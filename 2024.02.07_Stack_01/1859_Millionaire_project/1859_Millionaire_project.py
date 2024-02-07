import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr_re = arr[::-1]
    profit = 0
    max_cost = arr_re[0]
    for n in range(N):
        if arr_re[n] > max_cost:
            max_cost = arr_re[n]
        else:
            profit += max_cost - arr_re[n]
    print(f'#{t} {profit}')
    # for n in range(N):
    #     if arr_re[n] > arr_re[n + 1]:
    #         if max_cost > arr_re[n]:
    #             storage.append(arr_re[n])
    #         elif max_cost < arr_re[n]:
    #             max_cost = arr_re[n]
    #     elif arr_re[n] <= arr_re[n + 1]:
    #         if max_cost > arr_re[n]:
    #             profit += max_cost * len(storage)
    #             max_cost = arr_re[n]
    #             continue
    #         elif arr_re[n] < arr_re[n + 1]:
    #             storage.append(arr_re[n])
    #     elif arr_re[n] == arr_re[n + 1]:
    #         continue
    # print(profit)
    # if arr[0] <= arr[1]:
    #     cnt += 1
    #     total_cost += arr[0]
    # for n in range(1, N):
    #     if total_cost == 0:
    #         if arr[n] > arr[n + 1]:
    #             continue
    #         elif arr[n] <= arr[n + 1]:
    #             total_cost += arr[n]
    #             cnt += 1
    #     elif total_cost != 0:
    #         if arr[n] > arr[n + 1]:
    #             profit += arr[n - 1] * cnt - total_cost
    #             total_cost = 0
    #             cnt = 0
    #         elif arr[n] <= arr[n + 1]:
    #             total_cost += arr[n]
    #             cnt += 1