import sys
sys.stdin = open('4874_input.txt')

T = int(input())

for t in range(1, T + 1):
    fx = list(map(str, input().split()))

    cnt_num = 0
    cnt_str = 0
    for i in fx:
        if i.isnumeric():
            cnt_num += 1
        if i in '*/+-':
            cnt_str += 1

    if cnt_num - cnt_str != 1:
        print(f'#{t} error')
        continue

    stack = []
    for tk in fx:
        if tk == '.':
            result = stack[0]
            break
        if tk.isnumeric():
            stack.append(int(tk))
        elif tk != ' ':
            n2 = stack.pop()
            n1 = stack.pop()
            if tk == '+':
                res = n1 + n2
            elif tk == '-':
                res = n1 - n2
            elif tk == '*':
                res = n1 * n2
            elif tk == '/':
                res = n1 // n2
            stack.append(res)
    print(f'#{t} {result}')