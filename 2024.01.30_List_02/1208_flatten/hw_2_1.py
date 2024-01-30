import sys
sys.stdin = open('input.txt')

def BubbleSort(a, N):               # 정렬할 배열과 배열의 크기
    for i in range(N - 1, 0, -1):   # 정렬될 구간의 끝
        for j in range(0, i):       # 비교할 원소 중 왼쪽 원소의 인덱스
            if a[j] > a[j + 1]:     # 왼쪽 원소가 더 크면
                a[j], a[j + 1] = a[j +1], a[j]
    return a

tc = 10
for T in range(1, tc + 1):
    N = int(input())
    boxes = list(map(int, input().split()))


    for i in range(N):
        BubbleSort(boxes, 100)
        boxes[0] += 1
        boxes[99] -= 1

    BubbleSort(boxes, 100)
    dif = boxes[99] - boxes[0]
    print(f'#{T} {dif}')
    #     for j in range(len(boxes)):
    #         new_list = []
    #         max_h = 0
    #         min_h = 101
    #         if max_h < boxes[j]:
    #             max_h = boxes[j]
    #             a = boxes.index(max_h)
    #
    #         if min_h > boxes[j]:
    #             min_h = boxes[j]
    #             b = boxes.index(min_h)
    #
    #         boxes[a] -= 1
    #         boxes[b] += 1
    # print(boxes[a], boxes[b])
    #
    #
    # dif = boxes[a] - boxes[b]
    # print(f'#{T} {dif}')