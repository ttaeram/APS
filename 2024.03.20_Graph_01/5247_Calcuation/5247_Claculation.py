import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    cnt = 0
    while N != M:
        if M - N >= N:
            N *= 2

        cnt += 1