import sys
sys.stdin = open('input.txt')

T = int(input())

def Pascal(n):
    pascal = [1]
    if n == 1:
        return pascal
    if n == 2:
        pascal = [1, 1]
        return pascal
    else:
        P1 = Pascal(n - 1)
        pascal = [1] * n
        for i in range(len(Pascal(n - 1)) - 1):
            pascal[i + 1] = P1[i] + P1[i + 1]
        return pascal

for t in range(1, T + 1):
    N = int(input())

    print(f'#{t}')
    for j in range(1, N + 1):
        print(*Pascal(j))
