import sys
sys.stdin = open('5203_input.txt')

T = int(input())
for t in range(1, T + 1):
    deck = ''.join(input().split())
    deck_1 = []
    deck_2 = []
    win_1 = 0
    win_2 = 0
    res = 0

    for i in range(12):
        if i % 2 == 0:
            deck_1.append(deck[i])
        else:
            deck_2.append(deck[i])
        if len(deck_1) >= 3:
            for j in range(len(deck_1)):
                if str(int(deck_1[j]) + 1) in deck_1 and str(int(deck_1[j]) + 2) in deck_1:
                    win_1 += 1
                if deck_1.count(deck_1[j]) >= 3:
                    win_1 += 1

            for k in range(len(deck_2)):
                if str(int(deck_2[k]) + 1) in deck_2 and str(int(deck_2[k]) + 2) in deck_2:
                    win_2 += 1
                if deck_2.count(deck_2[k]) >= 3:
                    win_2 += 1

        if win_1 > 0 and win_2 == 0:
            res = 1
            break
        elif win_2 > 0 and win_1 == 0:
            res = 2
            break
    if win_1 == 0 and win_2 == 0:
        res = 0

    print(f'#{t} {res}')