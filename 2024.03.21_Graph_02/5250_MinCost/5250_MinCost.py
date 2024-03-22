import sys
sys.stdin = open('5250_input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    des = [N - 1, N - 1]
    pos = [0, 0]
    cnt = 0

    # for r in range(N):
    #     for c in range(N):

    # while pos != des:

    print(arr)