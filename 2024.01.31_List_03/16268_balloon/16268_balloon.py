import sys
sys.stdin = open('input1.txt')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    balloon = []
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for n in range(N):
        element = list(map(int, input().split()))
        balloon.append(element)


    max_list = []
    for i in range(N):
        for j in range(M):
            sum_balloon = balloon[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    sum_balloon += balloon[ni][nj]
            max_list.append(sum_balloon)

    max_balloon = 0

    for a in max_list:
        if max_balloon < a:
            max_balloon = a

    print(f'#{t} {max_balloon}')