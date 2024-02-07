import sys
sys.stdin = open('4866_input.txt')

T = int(input())
example = ['(', ')', '{', '}', '[', ']']
example_left = ['(', '{', '[']
example_right = [')', '}', ']']

def bracket_check(bracket):
    stack = []
    for b in bracket:
        if len(stack) > 0:
            if b in example_left:
                stack.append(b)
            elif b in example_right:
                for n in range(3):
                    if b == example_right[n]:
                        if stack[-1] == example_left[n]:
                            stack.pop()
                        else:
                            return 0
        elif len(stack) == 0:
            if b in example_left:
                stack.append(b)
            elif b in example_right:
                return 0
    if len(stack) > 0:
        return 0
    return 1

for t in range(1, T + 1):
    sentence = input()
    bracket = []

    for s in sentence:
        if s in example:
            bracket.append(s)

    result = bracket_check(bracket)
    print(f'#{t} {result}')