n, m = map(int, input().split())
res = dict()
for i in range(1,n+1):
    for j in range(1,m+1):
        s = i + j
        res[s] = res.get(s, 0) + 1

max = 0
for v in res.values():
    if v > max:
        max = v
for k, v in res.items():
    if v == max:
        print(k, end=' ')
