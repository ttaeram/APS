import sys
sys.stdin = open('input.txt')

def bin_to_dec(BIN):
    res = 0
    BIN_rev = ''.join(reversed(BIN))
    for n in range(len(BIN_rev)):
        if BIN_rev[n] == '1':
            res += 2 ** n
    return res

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [input().strip() for n in range(N)]
    ans = []
    string = ''

    for m in arr:
        string += m

    for i in range(0, len(string), 7):
        str_sep = string[i:i+7]
        ans.append(bin_to_dec(str_sep))

    print(f'#{t}', *ans)