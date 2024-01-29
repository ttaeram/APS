import sys
sys.stdin = open('4835_input.txt')

T = int(input())   # Test Case가 주어지는 경우
# T = 10
for tc in range(1, T + 1):
    N, M = map(int, input().split())    # 정수의 개수 N, 구간의 개수 M이 주어짐
    arr = list(map(int, input().split()))

    max_num = 0
    min_num = 100000000
    for i in range(N - (M - 1)):
        sum_num = 0
        for j in arr[i:i+M]:
            sum_num += j
        if sum_num < min_num:
            min_num = sum_num
        if sum_num > max_num:
            max_num = sum_num

    print(f'#{tc} {max_num - min_num}')
