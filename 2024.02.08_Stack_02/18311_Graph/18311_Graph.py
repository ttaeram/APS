import sys
sys.stdin = open('input.txt')

def DFS(i, V):
    visited = [0] * (V + 1)
    st = []
    visited[i] = 1
    print(i, end = '')
    while True:
        for w in adjl[i]:
            if visited[w] == 0:
                st.append(i)
                i = w
                visited[i] = 1
                print(f'-{i}', end = '')
                break
        else:
            if st:
                i = st.pop()
            else:
                break
    return

V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjl = [[] for _ in range(V + 1)]
for i in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)

print('#1', end = ' ')
DFS(1, V)