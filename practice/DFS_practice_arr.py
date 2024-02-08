# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

# 주로 인풋은 간선(E), 정점(V) 정보를 같이 줌
# 인접 배열을 저장할 때는 간선의 정보를 이용해서 저장하면 됨
# 인접 배열을 초기화할 때는 정점 정보를 이용하면 됨

V, E = 7, 8
edge_list = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# 정점의 개수만큼 2차원 리스트로 만들면 됨
# 0은 연결되어 있지 않음을 의미
# 1은 연결되어 있음을 의미
adj_arr = [[0] * (V + 1) for _ in range(V + 1)]

for idx in range(E):
    # 시작점(idx * 2), 도착점(idx * 2 + 1)
    start = edge_list[idx * 2]
    end = edge_list[idx * 2 + 1]
    # 인접 배열
    adj_arr[start][end] = 1
    # 만약 양방향으로 저장해야 한다면
    # adj_arr[end][start] = 1

for i in range(V + 1):
    print(*adj_arr[i])