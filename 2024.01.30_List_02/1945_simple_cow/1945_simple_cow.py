import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    div = [2, 3, 5, 7, 11]
    result = [0] * 5

    while N != 1:
        for n in range(5):
            if N % div[n] == 0:
                N = N // div[n]
                result[n] += 1


    print(f'#{t}', *result)