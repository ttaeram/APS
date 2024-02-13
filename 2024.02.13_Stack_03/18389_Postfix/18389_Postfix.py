import sys
sys.stdin = open('input.txt')

t = int(input())
fx = str(input())
postfix = ''
top = -1
stack = []

for tk in fx:
    if tk in '*/+-':
        stack.append(tk)
    else:
        postfix += tk

for a in stack[::-1]:
    postfix += a

print(f'#{t} {postfix}')