import sys
sys.stdin = open('input.txt')

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    p = arr[len(arr) // 2]
    left = []
    mid = []
    right = []
    for n in arr:
        if n < p:
            left.append(n)
        elif n > p:
            right.append(n)
        else:
            mid.append(n)
    return quicksort(left) + mid + quicksort(right)

T = int(input())
for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    l = 0
    r = len(arr) - 1
    n_arr = quicksort(arr)
    print(f'#{t}', end = ' ')
    print(*n_arr)
