from collections import deque
import sys
sys.stdin = open('input.txt')

for i in range(10):
    t = int(input())
    num = deque(map(int, input().split()))

    while True:
        for j in range(1, 6):
            number = num.popleft() - j
            if number <= 0:
                number = 0
                num.append(number)
                break
            else:
                num.append(number)
        if 0 in num:
            break

    print(f'#{t}', *num)