import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cards = list(map(str, input().split()))
    if N % 2 == 0:
        half = N // 2
    else:
        half = N // 2 + 1
    deck_1 = []
    deck_2 = []
    new_deck = []
    for i in range(half):
        deck_1.append(cards[i])
    for j in range(half, N):
        deck_2.append(cards[j])

    for k in range(half):
        if k >= len(deck_2):
            new_deck.append(deck_1[k])
            break
        new_deck.append(deck_1[k])
        new_deck.append(deck_2[k])

    print(f'#{t}', end = ' ')
    print(*new_deck)