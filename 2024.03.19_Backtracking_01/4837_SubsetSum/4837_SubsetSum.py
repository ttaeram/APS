import sys
sys.stdin = open('4837_input.txt')

def subset(num):
    global ans
    result = []
    if num == 12:
        for i in range(12):
            if check[i] == 1:
                result.append(A[i])
        if len(result) == N:
            if sum(result) == K:
                ans += 1
        return
    check[num] = 1
    subset(num + 1)
    check[num] = 0
    subset(num + 1)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    check = [0] * 12
    ans = 0
    subset(0)
    print(f'#{t} {ans}')