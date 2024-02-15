from collections import deque
import sys
sys.stdin = open('5097_input.txt')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    num = deque(map(int, input().split()))

    for i in range(M):
        num.append(num.popleft())

    res = num[0]
    print(f'#{t} {res}')