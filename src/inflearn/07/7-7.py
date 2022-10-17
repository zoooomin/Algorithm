#송아지 찾기(BFS)
from collections import deque
max = 10000
s, e = map(int, input().split())
ch = [0] * (max+1)
dis = [0] * (max+1)
ch[s] = 1
dis[s] = 0
dQ = deque()
dQ.append(s)
while dQ:
    now = dQ.popleft()
    if now == e:
        break
    for i in (now-1, now+1, now+5):
        if 0 < i <= max:
            if ch[i] == 0:
                ch[i] = 1
                dis[i] = dis[now] + 1
                dQ.append(i)

print(dis[e])