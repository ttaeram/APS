import sys
sys.stdin = open('input.txt')

def preorder(t):
    if t:
        print(t, end = ' ')
        preorder(L[t])
        preorder(R[t])

V = int(input())
arr = list(map(int, input().split()))
E = V - 1
L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)

for i in range(E):
    p, c = arr[2 * i], arr[2 * i + 1]
    if L[p] == 0:
        L[p] = c
    else:
        R[p] = c
    P[c] = p

C = V
while P[C] != 0:
    C = P[C]
root = C
preorder(root)