import sys
sys.stdin = open('input.txt')

T = 10

for t in range(1, T + 1):
    N = int(input())
    fx = input()
    postfix = ''
    stack = []
    priority = {'*': 2, '+': 1}

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
    for x in postfix:
        if x.isnumeric():
            stack_2.append(int(x))
        elif x in priority:
            x2 = stack_2.pop()
            x1 = stack_2.pop()
            if x == '*':
                stack_2.append(x1 * x2)
            elif x == '+':
                stack_2.append(x1 + x2)
    result = stack_2[0]

    print(f'#{t} {result}')