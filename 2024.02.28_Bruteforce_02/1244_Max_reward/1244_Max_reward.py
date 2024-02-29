import sys
sys.stdin = open('input.txt')

def perm(time):      # 재귀 도는 횟수 == 숫자를 바꾸는 횟수
    global max_v, cnt
    value = int(''.join(number))
    if value in checked[time]:
        return
    checked[time].add(value)   # 체크된 적 없으면 등록

    if time == limit:    # 바꾸는 위치가 N만큼 되면 재귀 종료 / N: 리스트 길이
        # 최댓값인지 확인
        if max_v < value:
            max_v = value
        return
    else:
        # 교환할 index를 위해 for하나 추가
        for i in range(N):
            for j in range(i + 1, N):  # 자기 자리를 교환 위치로 보면 안되기 때문에
                number[i], number[j] = number[j], number[i]
                perm(time + 1)
                number[i], number[j] = number[j], number[i]

T = int(input())
for t in range(1, T + 1):
    # map(int, input().split()) 을 하게 되면 number 가 list 로 변환하기 복잡
    number, limit = input().split()
    number = list(number)
    limit = int(limit)
    N = len(number)
    max_v = 0
    checked = [set() for _ in range(limit + 1)]

    perm(0)
    print(f'#{t} {max_v}')
    # puzzle, N = map(str, input().split())
    # N = int(N)
    #
    # for n in range(N):
    #     index = puzzle.idx(max(puzzle))
    #     if index != 0:
    #         puzzle[0], puzzle[index] = puzzle[index], puzzle[0]
    #     if index == 0:
    #         new_index = puzzle.idx(max(puzzle[index + 1::]))
    #         puzzle[index + 1], puzzle[index] = puzzle[index], puzzle[1]