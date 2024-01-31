import sys
sys.stdin = open('input1.txt')

di = [0, 1, 0, -1]  # 방향별로 더할 값
dj = [1, 0, -1, 0]


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    balloon = []

    for n in range(N):
        element = list(map(int, input().split()))
        balloon.append(element)

    sum_balloon = 0
    max_list = []
    for i in range(N):
        for j in range(M):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    sum_balloon += balloon[ni][nj]
                sum_balloon += balloon[i][j]
                max_list.append(sum_balloon)

    max_balloon = 0
    for maxs in max_list:
        if max_balloon < maxs:
            max_balloon = maxs

    print(max_balloon)