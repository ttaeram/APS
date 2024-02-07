import sys
sys.stdin = open('4873_input.txt')

T = int(input())

for t in range(1, T + 1):
    word = input()
    letter = []
    for w in word:
        letter.append(w)

    new_word = [letter[0]]
    i = 1
    for n in range(1, len(letter)):
        new_word.append(letter[n])
        if len(new_word) >= 2:
            if new_word[i] == new_word[i - 1]:
                new_word.pop()
                new_word.pop()
                i -= 2
        i += 1
    result = len(new_word)
    print(f'#{t} {result}')