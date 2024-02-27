import sys
sys.stdin = open('5188_input.txt')

def search(x, y, s):
    global min_sum
    s += arr[x][y]
    if s > min_sum:
        return
    if x == N - 1 and y == N - 1:
        if min_sum > s:
            min_sum = s
        return
    if x < N - 1:
        search(x + 1, y, s)
    if y < N - 1:
        search(x, y + 1, s)

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 10000000

    search(0, 0, 0)
    print(f'#{t} {min_sum}')