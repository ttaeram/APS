import sys
sys.stdin = open('input.txt')

def inorder(T):
    if T:
        inorder(left[T])
        inorder(right[T])
        ans.append(arr[T])

T = 10
for t in range(1, T + 1):
    N = int(input())
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    par = [0] * (N + 1)
    arr = [0] * (N + 1)
    ans = []

    for n in range(N):
        info = input().split()

        idx = int(info[0])
        value = info[1]
        arr[idx] = value

        if len(info) >= 3:
            left[idx] = int(info[2])
            par[int(info[2])] = idx
            if len(info) == 4:
                right[idx] = int(info[3])
                par[int(info[3])] = idx

    inorder(1)

    stack = []
    for x in ans:
        if x.isnumeric():
            stack.append(int(x))
        else:
            x2 = stack.pop()
            x1 = stack.pop()
            if x == '*':
                stack.append(x1 * x2)
            elif x == '/':
                stack.append(x1 // x2)
            elif x == '+':
                stack.append(x1 + x2)
            elif x == '-':
                stack.append(x1 - x2)

    res = stack[0]
    print(f'#{t} {res}')

    # postfix = []
    # stack = []
    # stack_2 = []
    # priority = {'*': 2, '/': 2, '+': 1, '-': 1}
    #
    # for tk in ans:
    #     if tk.isnumeric():
    #         postfix.append(tk)
    #     elif tk in priority:
    #         if stack and (priority[tk] <= priority[stack[-1]]):
    #             postfix.append(stack.pop())
    #         stack.append(tk)
    #
    # while stack:
    #     postfix.append(stack.pop())
    #
    # for x in postfix:
    #     if x.isnumeric():
    #         stack_2.append(int(x))
    #     elif x in priority:
    #         x2 = stack_2.pop()
    #         x1 = stack_2.pop()
    #         if x == '*':
    #             stack_2.append(x1 * x2)
    #         elif x == '/':
    #             stack_2.append(x1 / x2)
    #         elif x == '+':
    #             stack_2.append(x1 + x2)
    #         elif x == '-':
    #             stack_2.append(x1 - x2)
    #
    # res = stack_2[0]
    # print(res)
