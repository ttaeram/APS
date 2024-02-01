import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = []

    for n in range(N):
        element = list(map(int, input().split()))
        arr.append(element)

    new_arr = []
    for i in range(N):
        new_element = []
        for j in range(N-1, -1, -1):
            new_element.append(arr[j][i])
        for k in range(N-1, -1, -1):
            new_element.append(arr[k][::-1])
            new_arr.append(new_element)
    for m in range(N-1, -1, -1):
        new_1 = []
        for l in range(N):
            new_1.append(arr[l][m])

        print(new_1)
