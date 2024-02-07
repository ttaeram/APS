import sys
sys.stdin = open('input.txt')

T = int(input())

def bracket_check(bracket):
    stack = []
    for b in bracket:
        if len(stack) > 0:
            if b == '(':
                stack.append(b)
            elif b == ')':
                stack.pop()
        elif len(stack) == 0:
            if b == '(':
                stack.append(b)
            elif b == ')':
                return -1
    if len(stack) > 0:
        return -1
    return 1

for t in range(1, T + 1):
    bracket = input()
    result = bracket_check(bracket)
    print(f'#{t} {result}')