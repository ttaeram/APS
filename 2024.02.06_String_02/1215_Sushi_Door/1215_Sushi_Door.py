import sys
sys.stdin = open('input.txt')

T = 10

for t in range(1, T + 1):
    M = int(input())
    N = 8
    arr1 = [input() for _ in range(N)]
    arr2 = []

    for col in range(N):        # 세로줄
        str1 = ''
        for row in range(N):
            str1 += arr1[row][col]
        arr2.append(str1)

    cnt = 0
    for wo in arr1:
        for i in range(N-M + 1):
            word1 = wo[i:i+M]
            if word1 == word1[::-1]:
                cnt += 1

    for wos in arr2:
        for j in range(N-M + 1):
            word2 = wos[j:j+M]
            if word2 == word2[::-1]:
                cnt += 1

    print(f'#{t} {cnt}')
    # for col in range(N):
    #     str1 = ''
    #     for row in range(N):
    #         str1 += arr1[row][col]
    #     arr2.append(str1)
    # if N == M:
    #     for word in arr1:
    #         if word == word[::-1]:
    #             print(f'#{t} {word}')
    #
    #     for word in arr2:
    #         if word == word[::-1]:
    #             print(f'#{t} {word}')
    # else:
    #     for wo, wo2 in zip(arr1, arr2):
    #         for i in range(N-M+1):
    #             word2 = wo[i:i+M]
    #             word3 = wo2[i:i+M]
    #             if word2 == word2[::-1]:
    #                 print(f'#{t} {word2}')
    #             if word3 == word3[::-1]:
    #                 print(f'#{t} {word3}')