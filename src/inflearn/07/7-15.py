#토마토(BFS)
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
m, n = map(int, input().split())
tmt = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*m for _ in range(n)] #최소 날짜 구하기 위한 리스트
Q = deque()
cnt = 0
for i in range(n):
    for j in range(m):
        if tmt[i][j] == 1:
            Q.append((i, j))

while Q:
    tmp = Q.popleft()
    for t in range(4):
        xx = tmp[0] + dx[t]
        yy = tmp[1] + dy[t]
        if 0<=xx<n and 0<=yy<m and tmt[xx][yy] == 0:
            tmt[xx][yy] = 1
            ch[xx][yy] = ch[tmp[0]][tmp[1]] + 1
            Q.append((xx, yy))

flag = 1
for i in range(n):
    for j in range(m):
        if tmt[i][j] == 0:
            flag = 0

result = 0
if flag == 1:
    for i in range(n):
        for j in range(m):
            if ch[i][j] > result:
                result = ch[i][j]
    print(result)

else:
    print(-1)


