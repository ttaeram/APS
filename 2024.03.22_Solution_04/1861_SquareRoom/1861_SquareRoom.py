import sys
sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    cnt_lst = []
    for r in range(N):
        for c in range(N):
            num = arr[r][c]
            pos = arr[r][c]
            start = [r, c]
            direction = [r, c]
            cnt = 1

            while True:
                flag = True
                for i in range(4):
                    nr = direction[0] + dr[i]
                    nc = direction[1] + dc[i]
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] == pos + 1:
                            pos = arr[nr][nc]
                            direction = [nr, nc]
                            flag = False
                            cnt += 1
                if flag:
                    break
            max_cnt = max(cnt, max_cnt)
            if cnt < max_cnt:
                continue
            elif 1 < cnt:
                cnt_lst.append([num, cnt])
    cnt_lst.sort(key = lambda x: (-x[1], x[0]))
    ans = cnt_lst[0]
    print(f'#{t}', *ans)