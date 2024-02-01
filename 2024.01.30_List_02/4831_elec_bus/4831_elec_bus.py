import sys
sys.stdin = open('4831_input.txt')

def bus_brrr(K, N, bus_station):
    charge_cnt = 0
    current = 0
    for idx in range(N+1):
        for k in range(K, -1, -1):
            if current > idx:
                break
            elif current+K >= N:
                return charge_cnt
            elif current == idx:
                if idx + k == idx:
                    return 0
                elif bus_station[idx + k] == K:
                    charge_cnt += 1
                    current = idx + k
                    break
                else:
                    continue

T = int(input())
for t in range(1, T + 1):
    K, N, M = map(int, input().split())
    bus_stop = list(map(int, input().split()))

    bus_station = [0] *(N + 1)
    for n in range(N + 1):
        if n in bus_stop:
            bus_station[n] = K
    result = bus_brrr(K, N, bus_station)
    print(f'#{t} {result}')
# def min_charging_stations(K, N, M, stations):
#     for i in range(M - 1, 0, -1):  # 정렬될 구간의 끝
#         for j in range(0, i):  # 비교할 원소 중 왼쪽 원소의 인덱스
#             if stations[j] > stations[j + 1]:  # 왼쪽 원소가 더 크면
#                 stations[j], stations[j + 1] = stations[j + 1], stations[j]
#
#     print(stations)
#     current_station = 0  # 현재 위치
#     charge_count = 0  # 충전 횟수
#
#     for num in range(M):
#         distance = stations[num] - current_station
#
#         if distance > K:
#             # 현재 위치에서 다음 충전기까지의 거리가 최대 이동 가능 거리보다 크면 충전이 필요하다.
#             return 0
#         # if distance <= K:
#         # 현재 충전기까지 갈 수 있으므로 계속 진행한다.
#         current_station = stations[num]
#         K -= distance   # 충전을 했으므로 최대 이동 가능 거리를 감소시킨다.
#
#         # 종점에 도착했는지 확인
#         if current_station + K >= N:
#             return charge_count
#
#         charge_count += 1
#
#     # 마지막 충전기 이후에도 종점에 도착하지 않았다면 0을 반환한다.
#     return 0


    # charge_cnt = 0
    # current = 0
    # for idx in range(N):
    #     for k in range(K, 0, -1):
    #         if current > idx:
    #             continue
    #         elif current == idx:
    #             if current >= N:
    #                 print(f'#{t} {charge_cnt}')
    #                 break
    #             if bus_station[idx + k] == K:
    #                 charge_cnt += 1
    #                 currnet = idx + k
    #             else:
    #                 print(f'#{t} 0')
    #                 break

