import sys
sys.stdin = open('input.txt')

def subset(num):
    global ans
    result = []
    if num == l:
        for a in range(l):
            if check[a] == 1:
                result.append(arr[a])
        if sum(result) == 0:
            ans += 1
        return
    check[num] = 1
    subset(num + 1)
    check[num] = 0
    subset(num + 1)

T = 1
arr = list(map(int, input().split()))
l = len(arr)
check = [0] * l
ans = 0
subset(0)
print(f'#{T} {ans}')
