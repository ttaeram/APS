import sys
sys.stdin = open('4875_input.txt')

# 목적이 출구에 도착할 수 있는지 여부이므로 (Backtracking)
# DFS: 모든 정점을 방문
def find_start():
    for r in range(N):
        for c in range(N):
            if maze[r][c] == '2':
                return r, c


def find_path(row, col):
    global result
    if result:      # 이미 도착한 경우
        return

    # 델타 탐색
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != '1':
            if maze[nr][nc] == '3':
                result = 1
                return
            elif maze[nr][nc] == '0':
                maze[nr][nc] = '1'
                find_path(nr, nc)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input().strip()) for _ in range(N)]

    # 델타 탐색을 위한 상,하,좌,우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 시작 위치를 찾아야됨
    r, c = find_start()
    result = 0
    find_path(r, c)

    print(f'#{tc} {result}')

# class Stack:
#     def __init__(self, size):
#         self.top = -1
#         self.stack = [0] * size
#
#     def peek(self):
#         # top 이 마지막 인덱스에 위치해 있는지 비교
#         return self.top == len(self.stack) - 1
#
#     def is_empty(self):
#         return self.top == -1
#
#     def push(self, value):
#         if self.is_full():
#             print('Full~~~~~')
#             return 0
#         else:
#             self.top += 1
#             self.stack[self.top] = value
#
#     def pop(self):
#         if self.is_empty():
#             print('Empty~~~~~')
#             return 0
#
# def find_start():
#     for r in range(N):
#         for c in range(N):
#             if maze[r][c] == '2':
#                 return r, c

# for i in range(N):
#     for j in range(N):
#         if maze[i][j] == 0:
#             road.append([i, j])
#         if maze[i][j] == 2:
#             start = [i, j]
#         if maze[i][j] == 3:
#             goal = [i, j]
#
# res = goal
# cnt = 0
# while [res[0] + 1, res[1]] != start and [res[0] - 1, res[1]] != start and [res[0], res[1] + 1] != start and [res[0], res[1] - 1] != start:
#     if [res[0] + 1, res[1]] in road:
#         road.remove([res[0] + 1, res[1]])
#         res = [res[0] + 1, res[1]]
#     elif [res[0] - 1, res[1]] in road:
#         road.remove([res[0] - 1, res[1]])
#         res = [res[0] - 1, res[1]]
#     elif [res[0], res[1] + 1] in road:
#         road.remove([res[0], res[1] + 1])
#         res = [res[0], res[1] + 1]
#     elif [res[0], res[1] - 1] in road:
#         road.remove([res[0], res[1] - 1])
#         res = [res[0], res[1] - 1]
#     else:
#         res = goal
#     cnt += 1
#     if cnt > N ** 2:
#         print(f'#{t} 0')
#         exit(0)
#
# if [res[0] + 1, res[1]] == start or [res[0] - 1, res[1]] == start or [res[0], res[1] + 1] == start or [res[0], res[1] - 1] == start:
#     print(f'#{t} 1')
# else:
#     print(f'#{t} 0')

# for k in road:
#     if int(k[0]) < N - 1 or int(k[1]) < N - 1:
#         if str(int(k[0]) + 1) + k[1] not in road or k[0] + str(int(k[1]) + 1) not in road:
#             print(0)
#         else:
#             print(1)
