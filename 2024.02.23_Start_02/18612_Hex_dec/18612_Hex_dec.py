import sys
sys.stdin = open('input.txt')

hex_dec = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def hex_to_dec(HEX):
    global flag
    if HEX[0] == '0':
        flag = False

    HEX_rev = ''.join(reversed(HEX))
    res = 0
    for i in range(len(HEX_rev)):
        if HEX_rev[i].isdecimal():
            res += 16 ** i * int(HEX_rev[i])
        else:
            res += 16 ** i * hex_dec[HEX_rev[i]]
    return res

def dec_to_bin(DEC):
    global flag
    res = ''
    while DEC != 0:
        value = DEC % 2
        if value == 0:
            res = '0' + res
        else:
            res = '1' + res
        DEC //= 2

    if not flag:
        res = '0' * 7 + res
    return res

def bin_to_dec(BIN):
    res = 0
    BIN_rev = ''.join(reversed(BIN))
    for n in range(len(BIN_rev)):
        if BIN_rev[n] == '1':
            res += 2 ** n
    return res

T = int(input())
for t in range(1, T + 1):
    HEX = input().strip()
    DEC = hex_to_dec(HEX)
    BIN = dec_to_bin(DEC)
    ans = []
    flag = True

    i = 0
    while i < len(BIN) - 7:
        pw = BIN[i:i + 7]
        ans.append(bin_to_dec(pw))
        i += 7
    if i != len(BIN) - 7:
        pw = BIN[i:len(BIN)]
        ans.append(bin_to_dec(pw))

    print(f'#{t}', *ans)