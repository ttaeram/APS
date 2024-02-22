import sys
sys.stdin = open('5186_input.txt')

def dec_to_bin(DEC):
    res = ''
    while True:
        if len(res) == 13:
            return 'overflow'
        if DEC == 0.5:
            res += '1'
            return res
        elif DEC > 0.5:
            res += '1'
            DEC = DEC * 2 - 1
        else:
            res += '0'
            DEC *= 2

T = int(input())
for t in range(1, T + 1):
    DEC = float(input())
    ans = dec_to_bin(DEC)
    print(f'#{t} {ans}')