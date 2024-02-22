import sys
sys.stdin = open('input.txt')

T = 10
for t in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    new_table = []
    for c in range(N):
        new = []
        for r in range(N):
            if table[r][c] == 1 or table[r][c] == 2:
                new.append(table[r][c])
        new_table.append(new)

    cnt = 0
    for i in range(N):
        # for j in range(len(new_table[i])):
        j = 0
        while True:
            if j == len(new_table[i]):
                break

            if new_table[i][0] == 2:
                k = 0
                while new_table[i][k] != 2:
                    new_table[i][k] = 0
                    k += 1
            if new_table[i][-1] == 1:
                k = -1
                while new_table[i][k] != 1:
                    new_table[i][k] = 0
                    k -= 1

            if new_table[i][j] == 0:
                j += 1
            else:
                if new_table[i][j] == 1 and j < len(new_table[i]) - 1:
                    if new_table[i][j + 1] == 1:
                        j += 1
                        continue
                    elif new_table[i][j + 1] == 2:
                        cnt += 1

                # if new_table[i][j] == 2 and j < len(new_table[i]) - 1:
                #     if new_table[i][j + 1] == 2:
                #         j += 1
                #         continue
                #     elif new_table[i][j + 1] == 1:
                #         cnt += 1
            j += 1
    print(f'#{t} {cnt}')