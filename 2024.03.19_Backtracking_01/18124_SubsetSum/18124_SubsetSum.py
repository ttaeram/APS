import sys
sys.stdin = open('input.txt')

def subset(num):
    global ans
    result = []
    if num == l:
        for r in range(l):
            if check[r] == 1:
                result.append(arr[r])
        if len(result) > 0:
            if sum(result) == 0:
                ans = 1
        return
    check[num] = 1
    subset(num + 1)
    check[num] = 0
    subset(num + 1)

T = int(input())
for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    l = len(arr)
    check = [0] * l
    ans = 0

    subset(0)
    print(f'#{t} {ans}')