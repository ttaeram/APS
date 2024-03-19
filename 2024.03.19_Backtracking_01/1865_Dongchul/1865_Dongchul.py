import sys
sys.stdin = open('input.txt')

def subset(num, res):
    global ans
    if ans >= res:
        return

    if num == N:
        ans = max(res,ans)
        return

    for i in range(num, N):
        idx[num], idx[i] = idx[i], idx[num]
        subset(num + 1, res * arr[num][idx[num]] * 0.01)
        idx[num], idx[i] = idx[i], idx[num]

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    idx = [j for j in range(N)]
    ans = 0
    subset(0, 1)
    print(f'#{t} %6f'%round(ans * 100, 6))
    # if ~~~~:
    #     return
    # 너꺼 마지막에 리스트 다차면
    # res 계산이야?
    # 그럼
    # 중간에 곱셉값
    # 확인할 수 있는
    # 방법
    # 없어?
    # 리스트에 1개 넣고 곱하고 1개넣고 곱하고 이렇게해야대
    # 그래서 중간에 곱한 값이 처음 max_val보다 작으면 걔는 돌필요 없자나
    # 그렇게 끊어줘야대 위에 if 문 넣어서 return  해서서
