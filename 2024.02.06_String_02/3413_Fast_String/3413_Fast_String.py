import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T + 1):
    A, B = map(str, input().split())

    cnt = 0
    i = 0
    while i < len(A):
        if A[i:i+len(B)] == B:
            i += len(B)
            cnt += 1

        else:
            cnt += 1
            i += 1
    print(f'#{t} {cnt}')