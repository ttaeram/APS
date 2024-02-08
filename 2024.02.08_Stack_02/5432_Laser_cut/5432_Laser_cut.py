import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T + 1):
    bracket = input()
    stack = []
    cnt = 0
    iron = 0
    for b in bracket:
        if len(stack) == 0:
            if b == '(':
                stack.append(b)
                cnt += 1
                iron += 1
        else:
            if b == '(':
                stack.append(b)
                cnt += 1
                iron += 1
            elif b == ')':
                stack.pop()
                cnt -= 1
                iron += cnt
    print(iron)

# if ( 다음 바로 ) 오면 레이저
# () 나오기 전까지 ( 갯수 세면서 가다가 레이저 지지면 + 갯수
# ) 나오면 갯수 -1
