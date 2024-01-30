import sys
sys.stdin = open('4831_input.txt')

T = int(input())

for t in range(1, T + 1):
    K, N, M = map(int, input().split())
    bus_stop = list(map(int, input().split()))

    for b in range(len(bus_stop) - 1):
        if bus_stop[b + 1] > bus_stop[b] + K or bus_stop[M - 1] + K < N or bus_stop[0] < K:
            print(f'#{t}', 0)

