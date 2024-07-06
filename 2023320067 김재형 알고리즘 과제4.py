def EXTRACTMIN(Q, pkey):
    min_val = 1000000
    key = -1
    for i in Q:
        if pkey[i][1] < min_val:
            min_val = pkey[i][1]
            key = i
    return key
 
n = int(input())
m = int(input())
 
road = [0 for i in range(n)]
pkey = [0 for i in range(n)]
 
for i in range(n):
    road[i] = [-1 for k in range(n)]
    pkey[i] = [-1, 10000000]
 
for i in range(m):
    edge = raw_input().split(',')
    a = int(edge[0])
    b = int(edge[1])
    w = int(edge[2])
    road[a][b] = w
    road[b][a] = w
 
pkey[0][1] = 0
 
Q = [i for i in range(n)]
 
for i in range(n):
    u = EXTRACTMIN(Q, pkey)
    Q.remove(u)
    for i in range(n):
        if road[u][i] != -1:
            if i in Q:
                if road[u][i] < pkey[i][1]:
                    pkey[i][0] = u
                    pkey[i][1] = road[u][i]
 
for i in range(1, n):
    print(pkey[i][0])