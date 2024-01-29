import sys
sys.stdin = open('input.txt')

tc = 10
for i in range(tc):
    N = int(input())
    arr = list(map(int, input().split()))

    for n in range(2, len(arr) - 3):
        max_h = 0
        sec_h = 0
        for j in arr[n-2:n+2]:
            (j+1) - j
                max_h = j
