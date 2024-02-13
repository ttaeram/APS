import sys
sys.stdin = open('4875_input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    maze = [input() for _ in range(N)]
    road = []

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '0' or maze[i][j] == '2' or maze[i][j] == '3':
                road.append(str(i) + str(j))
    print(road)

    for k in road:
        if int(k[0]) < N - 1 or int(k[1]) < N - 1:
            if str(int(k[0]) + 1) + k[1] not in road or k[0] + str(int(k[1]) + 1) not in road:
                print(0)
            else:
                print(1)
