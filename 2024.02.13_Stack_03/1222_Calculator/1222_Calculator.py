import sys
sys.stdin = open('input.txt')

T = 10

for t in range(1, T + 1):
    N = int(input())
    fx = input()
    postfix = ''
    top = -1
    stack = []
    priority = {'*': 2, '/': 2, '+': 1, '-': 1}

    for tk in fx:
        if tk.isnumeric():
            postfix += tk
        elif tk in priority:
            if stack and (priority[tk] <= priority[stack[-1]]):
                postfix += stack.pop()
            stack.append(tk)

    while stack:
        postfix += stack.pop()

    stack_2 = []

    for n in postfix:
        if n.isnumeric():
            stack_2.append(int(n))
        elif n != ' ':
            n2 = stack_2.pop()
            n1 = stack_2.pop()
            if n == '+':
                result = n1 + n2
            stack_2.append(result)
    result = stack_2[0]
    print(f'#{t} {result}')