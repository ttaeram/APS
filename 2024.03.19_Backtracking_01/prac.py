# P = [1,2,3]
#
# P[i], P[j] = P[j],P[i]
#
#
# [1,2,3]
# [2,1,3]
# [3,2,1]
# [3,1,2]

b = [[73,21,21],[11,59,40],[24,31,83]]
P = [0,1,2]

def f(i,k,s):
    global min_val
    if s > min_val:
        return
    if i == k:
        min_val = s
        return
    for j in range(i,k):
        P[i], P[j] = P[j], P[i]
        f(i+1,k,s+b[i][P[i]])
        P[i], P[j] = P[j], P[i]
min_val = 10000000
f(0,3,0)
print(min_val)
