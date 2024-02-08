import sys
sys.stdin = open('4869_input.txt')

T = int(input())

def C_P(line):
    if line == 1:
        return 1
    if line == 2:
        return 3
    if line % 2 == 0:
        return C_P(line - 2) * 4 - 1
    elif line % 2 == 1:
        return C_P(line -2) * 4 + 1
for t in range(1, T + 1):
    N = int(input())
    line = N // 10

    result = C_P(line)
    print(f'#{t} {result}')