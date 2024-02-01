import sys
sys.stdin = open('input.txt')

T = 10

for t in range(1, T + 1):
    N = int(input())
    arr = []
    position_2 = 0
    for l in range(100):
        ladder = list(map(int, input().split()))
        arr.append(ladder)

    for j in range(100):
        if arr[99][j] == 2:
            position_2 = j

    for i in range(99, -1, -1):
        if position_2 < 99 and arr[i][position_2 + 1] == 1:
            while position_2 < 99:
                if arr[i][position_2 + 1] == 0:
                    break
                position_2 += 1

        elif position_2 > 0 and arr[i][position_2 - 1] == 1:
            while 0 <= position_2:
                if arr[i][position_2 - 1] == 0:
                    break
                position_2 -= 1
    print(f'#{t} {position_2}')
