import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T + 1):
    bracket = input()
    stack = []
    iron = 0
    bracket = bracket.replace('()', 'L')

    for b in bracket:
        if b == '(':
            stack.append(b)
            iron += 1
        elif b == 'L':
            iron += len(stack)
        elif b == ')':
            stack.pop()

    print(f'#{t} {iron}')

# if ( 다음 바로 ) 오면 레이저
# () 나오기 전까지 ( 갯수 세면서 가다가 레이저 지지면 + 갯수
# ) 나오면 갯수 -1
