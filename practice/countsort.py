def Counting_Sort(DATA, TEMP, k):
    # DATA []: 입력 배열(0 to k)
    # TEMP []: 정렬된 배열
    # COUNTS []: 카운트 배열
    COUNTS = [0] * (k + 1)

    for i in range(0, len(DATA)):
        COUNTS[DATA[i]] += 1

    for i in range(1, k + 1):
        COUNTS[i] += COUNTS[i - 1]

    for i in range(len(TEMP) - 1, -1, -1):
        COUNTS[DATA[i]] -= 1
        TEMP[COUNTS[DATA[i]]] = DATA[i]
    print(*temp)

N = 6
k = 9
data = [7, 2, 4, 5, 1, 3]
counts = [0] * (k + 1)
temp = [0] * N

Counting_Sort(data, temp, k)