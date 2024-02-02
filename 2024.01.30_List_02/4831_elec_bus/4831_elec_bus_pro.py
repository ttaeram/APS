import sys
sys.stdin = open('4831_input.txt')

T = int(input())
for t in range(1, T + 1):
    K, N, M = map(int, input().split())
    station = set(map(int, input().split()))
    # hash 접근 set 가 list 보다 in 연산자 사용이 유리
    charge = 0
    move = K
    last = 0

    while move < N:
        for _ in range(K):
            if move in station:
                charge += 1
                break
            move -= 1

        if last == move:
            charge = 0
            break

        last = move
        move += K

    print(f'#{t} {charge}')