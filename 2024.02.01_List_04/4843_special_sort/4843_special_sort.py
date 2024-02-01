import sys
sys.stdin = open('4843_input.txt')

T = int(input())

def selectionsort(a, N):
    for i in range(N-1):
        min_idx = i
        for j in range(i + 1, N):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    sort_arr = selectionsort(arr, N)
    sort_arr1 = sort_arr[0:int(N/2)]
    sort_arr2 = sort_arr[:int(N/2)-1:-1]

    special_arr = []
    for n in range(N):
        if n % 2 == 0:
            special_arr.append(sort_arr2[int(n/2)])
        elif n % 2 == 1:
            special_arr.append(sort_arr1[int(n//2)])

    print(f'#{t}', end = ' ')
    special_arr2 = special_arr[0:10]

    for r in special_arr2:
        print(r, end = ' ')
    print()