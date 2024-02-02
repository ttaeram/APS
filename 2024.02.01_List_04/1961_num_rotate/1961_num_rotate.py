import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{t}')
    new_1 = []
    for i in range(N):
        num_1 = []
        for j in range(N-1, -1, -1):
            num_1.append(arr[j][i])
        new_1.append(num_1)

    new_2 = []
    for o in range(N-1, -1, -1):
        num_2 = []
        for k in range(N-1, -1, -1):
            num_2.append(arr[o][k])
        new_2.append(num_2)

    new_3 = []
    for m in range(N-1, -1, -1):
        num_3 = []
        for l in range(N):
            num_3.append(arr[l][m])
        new_3.append(num_3)

    for i in range(N):
        print(*new_1[i], sep='',end=' ')
        print(*new_2[i], sep='',end=' ')
        print(*new_3[i], sep='',end='\n')
