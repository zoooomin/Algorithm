#섬나라 아일랜드(BFS)
from collections import deque
#상하좌우 and 대각선
dx = [-1,0,1,0,-1,-1,1,1]
dy = [0,1,0,-1,-1,1,1,-1]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
Q = deque()

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            Q.append((i, j))
            board[i][j] = 0
            while Q:
                a = Q.popleft()
                for p in range(8):
                    xx = a[0] + dx[p]
                    yy = a[1] + dy[p]
                    if 0<=xx<n and 0<=yy<n and board[xx][yy] == 1:
                        board[xx][yy] = 0
                        Q.append((xx, yy))
            cnt += 1

print(cnt)
