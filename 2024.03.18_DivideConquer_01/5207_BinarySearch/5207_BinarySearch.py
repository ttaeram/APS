import sys
sys.stdin = open('5207_input.txt')

def binarySearch(b):
    l = 0
    h = N - 1
    de = []
    while l <= h:
        mid = (l + h) // 2
        if A[mid] == b:
            return de
        elif A[mid] > b:
            h = mid - 1
            de.append(0)
        elif A[mid] < b:
            l = mid + 1
            de.append(1)
    return [2]

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0

    for b in B:
        flag = True
        de = binarySearch(b)
        for i in range(len(de) - 1):
            if de[i] == 0 and de[i + 1] == 0:
                flag = False
                break
            elif de[i] == 1 and de[i + 1] == 1:
                flag = False
                break
        if de == [2]:
            flag = False
        if flag:
            cnt += 1

    print(f'#{t} {cnt}')