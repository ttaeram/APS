import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    n = round(N ** (1 / 3), 3)
    ans = -1

    if int(n) == n:
        ans = int(n)

    print(f'#{t} {ans}')

    # for i in range(N//3 + 1):
    #     if i ** 3 == N:
    #         ans = i
    #         break
    #     else:
    #         continue