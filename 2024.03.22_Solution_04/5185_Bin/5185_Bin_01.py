import sys
sys.stdin = open('5185_input.txt')

hex_dec = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def hex_to_dec(HEX):
    HEX_rev = ''.join(reversed(HEX))
    res = 0
    for i in range(len(HEX_rev)):
        if HEX_rev[i].isdecimal():
            res += 16 ** i * int(HEX_rev[i])
        else:
            res += 16 ** i * hex_dec[HEX_rev[i]]
    return res

def dec_to_bin(DEC):
    res = ''
    while DEC != 0:
        value = DEC % 2
        if value == 0:
            res = '0' + res
        else:
            res = '1' + res
        DEC //= 2
    if len(res) % 4 != 0:
        res = '0' * (4 - len(res) % 4) + res
    return res

T = int(input())
for t in range(1, T + 1):
    N, HEX = map(str, input().split())

    DEC = hex_to_dec(HEX)
    BIN = dec_to_bin(DEC)
    print(f'#{t} {BIN}')