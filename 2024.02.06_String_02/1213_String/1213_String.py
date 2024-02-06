import sys
sys.stdin = open('test_input.txt', encoding='UTF-8')

for _ in range(10):
    t = int(input())
    str1 = input()
    str2 = input()
    cnt = 0

    n = len(str1)
    m = len(str2)

    i = 0
    j = 0

    while j < m - n + 1:
        if str1[i] == str2[j]:
            equal = 0
            for a in range(n):
                if str1[i + a] == str2[j + a]:
                    equal += 1
                else:
                    break
            if equal == n:
                cnt += 1
                i = 0
                j += n
            else:
                i = 0
                j += equal
        else:
            j += 1

    print(f'#{t} {cnt}')
# def find(pattern, char):
#     for i in range(len(pattern) -2, -1, -1):
#         if pattern[i] == char:
#             return len(pattern) - i - 1
#     return len(pattern)

# def Boyer_Moore(pattern, text):
#     M = len(pattern)
#     N = len(text)
#     i = 0
#     cnt = 0
#
#     while i <= N - M:   # 반복은 텍스트 길이 - 패턴 길이
#         j = M - 1
#         while j >= 0:
#             if pattern[j] != text[i + j]:
#                 move = find(pattern, text[i + M - 1])
#                 break
#             j = j - 1
#         if j == -1:
#             cnt += 1
#
#         else:
#             i += move
#     return cnt