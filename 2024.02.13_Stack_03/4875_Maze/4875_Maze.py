import sys
sys.stdin = open('4875_input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]
    road = []

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 0:
                road.append([i, j])
            if maze[i][j] == 2:
                start = [i, j]
            if maze[i][j] == 3:
                goal = [i, j]

    res = goal
    cnt = 0
    while [res[0] + 1, res[1]] != start and [res[0] - 1, res[1]] != start and [res[0], res[1] + 1] != start and [res[0], res[1] - 1] != start:
        if [res[0] + 1, res[1]] in road:
            road.remove([res[0] + 1, res[1]])
            res = [res[0] + 1, res[1]]
        elif [res[0] - 1, res[1]] in road:
            road.remove([res[0] - 1, res[1]])
            res = [res[0] - 1, res[1]]
        elif [res[0], res[1] + 1] in road:
            road.remove([res[0], res[1] + 1])
            res = [res[0], res[1] + 1]
        elif [res[0], res[1] - 1] in road:
            road.remove([res[0], res[1] - 1])
            res = [res[0], res[1] - 1]
        else:
            res = goal
        cnt += 1
        if cnt > N ** 2:
            print(f'#{t} 0')
            exit(0)

    if [res[0] + 1, res[1]] == start or [res[0] - 1, res[1]] == start or [res[0], res[1] + 1] == start or [res[0], res[1] - 1] == start:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')

    # for k in road:
    #     if int(k[0]) < N - 1 or int(k[1]) < N - 1:
    #         if str(int(k[0]) + 1) + k[1] not in road or k[0] + str(int(k[1]) + 1) not in road:
    #             print(0)
    #         else:
    #             print(1)
