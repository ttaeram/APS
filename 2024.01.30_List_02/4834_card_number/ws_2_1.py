import sys
sys.stdin = open('4834_input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    num = int(input())
    c = [0] * N * 2

    for i in range(N):
        c[num % 10] += 1
        num //= 10
    num = str(num)
    max_n = 0

    max_n_list = []
    for j in range(len(c)):
        if max_n <= c[j]:
            max_n = c[j]
            max_n_list.append(j)

    print(f'#{t} {max_n_list[-1]} {max_n}')
    # card_list = []
    # card_cnt = {}
    #
    # for i in range(N):
    #     card_list.append(int(i))
    #
    # card_set = list(set(card_list))
    #
    # for j in range(len(card_set)):
    #     cnt = 0
    #     if card_set[j] in card_list:
    #         cnt += 1
    #     card_cnt[card_set[j]] = cnt
    #
    # print(card_cnt)