import sys
sys.stdin = open('input.txt')

hex_dec = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
password = {'001101': '0', '010011': '1', '111011': '2', '110001': '3', '100011': '4',
            '110111': '5', '001011': '6', '111101': '7', '011001': '8', '101111': '9'}

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
    if res[0] == '1':
        res = '0' * 2 + res
    return res

T = int(input())
for t in range(1, T + 1):
    HEX = input().strip()
    DEC = hex_to_dec(HEX)
    BIN = dec_to_bin(DEC)

    i = 0
    ans = []
    while i < len(BIN) - 6:
        pw = BIN[i:i + 6]
        if pw in password:
            ans.append(password[pw])
            i += 6
        else:
            i += 1

    print(f'#{t}', *ans)