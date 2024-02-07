import sys
sys.stdin = open('input.txt')

T = 10

for t in range(1, T + 1):
    N, password = map(str, input().split())
    letter = []
    for pw in password:
        letter.append(pw)

    new_word = []
    i = 1
    for n in range(len(letter)):
        if n == 0:
            new_word.append(letter[n])
            continue
        new_word.append(letter[n])
        if len(new_word) >= 2:
            if new_word[i] == new_word[i - 1]:
                new_word.pop()
                new_word.pop()
                i -= 2
        i += 1
    result = ''
    for wo in new_word:
        result += wo
    print(f'#{t} {result}')