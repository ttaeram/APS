import sys
# from collections import deque
sys.stdin = open('5204_input.txt')

# def merge(l, r):
#     global cnt
#     result = deque()
#
#     while len(l) > 0 or len(r) > 0:
#         if len(l) > 0 and len(r) > 0:
#             if l[0] <= r[0]:
#                 result.append(l.popleft())
#             else:
#                 result.append(r.popleft())
#         elif len(l) > 0:
#             result.append(l.popleft())
#         elif len(r) > 0:
#             result.append(r.popleft())
#     return result

def merge_sort(length, arr):
    global cnt
    if length == 1:
        return arr
    # l = deque()
    # r = deque()
    m = length // 2

    l = arr[:m]
    r = arr[m:]

    l = merge_sort(len(l), l)
    r = merge_sort(len(r), r)

    if l[-1] > r[-1]:
        cnt += 1

    return sorted(l + r)

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    res = merge_sort(N, arr)

    print(f'#{t} {res[N // 2]} {cnt}')