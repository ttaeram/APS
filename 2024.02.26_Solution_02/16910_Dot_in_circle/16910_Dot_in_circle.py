import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cnt = 0
    for r in range(-N, N + 1):
        for c in range(-N, N + 1):
            if r ** 2 + c ** 2 <= N ** 2:
                cnt += 1
    print(f'#{t} {cnt}')