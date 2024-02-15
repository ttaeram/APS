from collections import deque
import itertools
import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cus = deque(sorted(arr))
    flag = True

    # 시간이 M초 증가할 때마다 붕어빵은 K개씩 증가
    # 손님 시간이 M보다 작으면 K만큼 손님 제거
    # 손님 수가 K보다 많으면 반복
    # 손님 수가 K보다 작거나 같으면 한번만

    if N <= K:
        for k in range(K):
            if k >= N:
                break
            else:
                if cus[k] == -1:
                    break

                elif cus[k] < M:
                    flag = False
                    break
                else:
                    cus.popleft()
                    cus.append(-1)

    else:
        cnt = 1
        while True:
            slice_cus = list(itertools.islice(cus, K))
            if cus[0] == -1:
                break
            if flag is False:
                break

            for i in range(K):
                if slice_cus[i] == -1:
                    break
                elif slice_cus[i] < cnt * M:
                    flag = False
                    break
                else:
                    cus.popleft()
                    cus.append(-1)
            cnt += 1

    if flag:
        print(f'#{t} Possible')
    else:
        print(f'#{t} Impossible')

    #     for c in range(K):
    #         if c < N:
    #             if cus[c] < M:
    #                 print(f'#{t} Impossible')
    #                 flag = False
    #                 break
    #             else:
    #                 cus.popleft()
    #                 cus.append(-1)
    #
    #     if not flag:
    #         break
    # if flag:
    #     print(f'#{t} Possible')
