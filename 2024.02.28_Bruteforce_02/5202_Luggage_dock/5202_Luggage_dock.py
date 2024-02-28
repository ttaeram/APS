import sys
sys.stdin = open('5202_input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    arr.sort(key = lambda x: x[1])
    stack = []

    for i in arr:
        if not stack:
            stack.append(i)
        else:
            if stack[-1][1] <= i[0]:
                stack.append(i)

    ans = len(stack)
    print(f'#{t} {ans}')
