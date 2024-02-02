import sys
sys.stdin = open('input1.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    num = input()
    cnt = 0
    max_n_list = []

    for n in range(N):
        if num[n] == '1':
            cnt += 1
            max_n_list.append(cnt)
        elif num[n] == '0':
            cnt = 0

    max_n = 0
    for max_ns in max_n_list:
        if max_n < max_ns:
            max_n = max_ns
    print(f'#{t} {max_n}')