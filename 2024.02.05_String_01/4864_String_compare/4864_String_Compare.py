import sys
sys.stdin = open('4864_input.txt')

T = int(input())

for t in range(1, T + 1):
    str1 = str(input())
    str2 = str(input())

    if str1 in str2:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')