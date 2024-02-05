import sys
sys.stdin = open('4861_input.txt')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr1 = [input() for _ in range(N)]
    arr2 = []

    for col in range(N):
        str1 = ''
        for row in range(N):
            str1 += arr1[row][col]
        arr2.append(str1)
    if N == M:
        for word in arr1:
            if word == word[::-1]:
                print(f'#{t} {word}')

        for word in arr2:
            if word == word[::-1]:
                print(f'#{t} {word}')
    else:
        for wo, wo2 in zip(arr1, arr2):
            for i in range(N-M+1):
                word2 = wo[i:i+M]
                word3 = wo2[i:i+M]
                if word2 == word2[::-1]:
                    print(f'#{t} {word2}')
                if word3 == word3[::-1]:
                    print(f'#{t} {word3}')

    # for i in range(N):
    #     for k in range(N-M):
    #         if arr[i] == arr[i][::-1]:
    #             print(f'#{t} ', end = '')
    #             for word in arr[i]:
    #                 print(word, end = '')
    #     j_list = []
    #     for j in range(M):
    #         j_list.append(arr[j][i])
    #     print(j_list)