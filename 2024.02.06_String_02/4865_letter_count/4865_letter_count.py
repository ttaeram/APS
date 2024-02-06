import sys
sys.stdin = open('4865_input.txt')

T = int(input())

for t in range(1, T + 1):
    str1 = input()
    str2 = input()
    counting = {}

    for a in str1:
        counting[a] = 0

    for b in str2:
        for c in counting.keys():
            if b == c:
                counting[c] += 1

    max_value = 0
    for d in counting.values():
        if max_value < d:
            max_value = d

    print(f'#{t} {max_value}')