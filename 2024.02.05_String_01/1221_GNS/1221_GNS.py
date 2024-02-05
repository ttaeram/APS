import sys
sys.stdin = open('GNS_test_input.txt')

T =  int(input())

Eng = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for t in range(1, T + 1):
    num = [0] * 10
    tc, length = map(str, input().split())
    num_list = list(map(str, input().split()))

    for nums in num_list:
        if nums == Eng[0]:
            num[0] += 1
        elif nums == Eng[1]:
            num[1] += 1
        elif nums == Eng[2]:
            num[2] += 1
        elif nums == Eng[3]:
            num[3] += 1
        elif nums == Eng[4]:
            num[4] += 1
        elif nums == Eng[5]:
            num[5] += 1
        elif nums == Eng[6]:
            num[6] += 1
        elif nums == Eng[7]:
            num[7] += 1
        elif nums == Eng[8]:
            num[8] += 1
        elif nums == Eng[9]:
            num[9] += 1

    print(tc)
    for n in range(10):
        print((Eng[n] + ' ') * num[n], end = '')
    print()