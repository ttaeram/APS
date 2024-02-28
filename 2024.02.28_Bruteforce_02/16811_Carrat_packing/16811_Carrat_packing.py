import sys
sys.stdin = open('sample_in.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))
    C_d = {}
    C_ = list(C_d.keys())
    flag = True
    S = 0
    M = 0
    L = 0
    for c in C:
        C_d[c] = C.count(c)

    for i in range(len(C_) // 3):
        S += C_d[C_[i]]
        if S > N // 2:
            ans = -1
            break
        for j in range(i, 2 * len(C_) // 3):
            M += C_d[C_[j]]
            if M > N // 2:
                ans = -1
                flag = False
                break
            for k in range(j, len(C_)):
                L += C_d[C_[k]]
                if L > N // 2:
                    ans = -1
                    flag = False
                    break
    min_ = min(abs(S - M), abs(M - L), abs(L - S))
    if flag:
        print(min_)
    else:
        print(ans)