def find_set(x):
    if parents[x] == x:
        return x
    # 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    # 같은 집합이면 pass
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

V, E = map(int, input().split())
# 간선 정보들을 모두 저장
edges = []
for _ in range(V):
    s, e, w = map(int, input().split())
    edges.append([s, e, w])
# 가중치를 기준으로 정렬
edges.sort(key=lambda x: x[2])
# 대표자 배열
parents = [i for i in range(V)]

# MST 완성 = 간선의 개수가 V - 1개 일때
cnt = 0
sum_weight = 0
# 간선 확인
for s, e, w in edges:
    # 싸이클 발생시 pass
    # 이미 같은 집합에 속해있다면 pass
    if find_set(s) == find_set(e):
        continue
    cnt += 1
    # 싸이클 없으면 방문 처리
    union(s, e)
    sum_weight += w

    # MST 완성: 간선의 개수 = V - 1
    if cnt == V:
        break
print(f'최소 비용: {sum_weight}')