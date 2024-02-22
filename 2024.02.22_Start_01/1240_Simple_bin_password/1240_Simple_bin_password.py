import sys
sys.stdin = open('input.txt')

password = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5,
            '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    ans = []
    for y in range(N):
        arr.append(input())

    for i in range(N):
        if '1' in arr[i]:
            tar = arr[i]

    for c in range(M - 1, -1, -1):
        if tar[c] == '1':
            tar_ = tar[c - 55:c + 1]
            break
    for l in range(0, 56, 7):
        ans.append(password[tar_[l:l + 7]])

    code_1 = 0
    code_2 = 0
    for k in range(8):
        if k % 2 == 0:
            code_1 += ans[k]
        else:
            code_2 += ans[k]

    code_3 = code_1 * 3 + code_2

    if code_3 % 10 == 0:
        res = code_1 + code_2
    else:
        res = 0

    print(f'#{t} {res}')
