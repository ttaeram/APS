import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    arr1 = [list(map(int, input().split())) for _ in range(9)]
    total = []
    for col in range(9):
        sum_row = []
        sum_col = []
        for row in range(9):
            sum_row.append(arr1[col][row])
            sum_col.append(arr1[row][col])
            sum_3x3 = []
            if row % 3 == 0 and col % 3 == 0:
                for i in range(3):
                    for j in range(3):
                        sum_3x3.append(arr1[col + i][row + j])

                total.append(len(set(sum_3x3)))
        total.append(len(set(sum_col)))
        total.append(len(set(sum_row)))

    if 8 in total:
        print(f'#{t} 0')
    else:
        print(f'#{t} 1')

    # arr2 = []
    # arr3 = []
    #
    # for col in range(9):        # 세로줄
    #     str1 = []
    #     for row in range(9):
    #         str1.append(arr1[row][col])
    #     arr2.append(str1)
    #
    # a_ = 0
    # b_ = 0
    # for a in range(3):
    #     str2 = []
    #     a_ += a
    #     b_ = 0
    #     for b in range(3):
    #         b_ += b
    #         str2.append(arr1[a_][b_])
    #
    #
    # breakbreak = 0
    # for i in range(9):
    #     for j in range(1, 10):
    #         if breakbreak == 1:
    #             break
    #
    #         if j not in arr1[i]:
    #             print(f'#{t} 0')
    #             breakbreak = 1
    #
    #         if j not in arr2[i]:
    #             print(f'#{t} 0')
    #             breakbreak = 1