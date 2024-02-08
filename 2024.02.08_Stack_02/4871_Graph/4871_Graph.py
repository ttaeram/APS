import sys
sys.stdin = open('4871_input.txt')

def DFS(i, V):                      # 시작 i, 마지막 V
    visited = [0] * (V + 1)         # visited, stack 생성 및 초기화
    st = []
    visited[i] = 1                  # 시작점 방문
    result = []
    result.append(i)
    # print(i)                        # 정점에서 할 일
    while True:
        for w in adj_list[i]:           # 현재 방문한 정점에 인접하고 방문 안한 정점 w가 있으면
            if visited[w] == 0:
                st.append(i)        # push(i), i를 지나서
                i = w               # w에 방문
                visited[i] = 1
                result.append(i)
                # print(i)
                break
        else:                       # i에 남은 인접 정점이 없으면
            if st:      # 스택이 비어있지 않으면 (지나온 정점이 남아 있으면)
                i = st.pop()
            else:       # 스택이 비어있으면 (출발점에서 남은 정점이 없으면)
                break
    return result

T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())
    arr = []
    for _ in range(E):
        a, b = map(int, input().split())
        arr.append(a)
        arr.append(b)
    S, G = map(int, input().split())

    adj_list = [[] for _ in range(V + 1)]
    for i in range(E):
        n1, n2 = arr[i * 2], arr[i * 2 + 1]
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)
    result = DFS(1, V)
    if S in result and G in result:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')