import sys
sys.stdin = open('5205_input.txt')

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
    N = int(input())
    arr = list(map(int, input().split()))
    A = quicksort(arr)
    print(f'#{t} {A[N // 2]}')