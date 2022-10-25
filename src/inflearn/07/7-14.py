#안전영역(DFS)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x, y, h):
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and ch[xx][yy] == 0 and board[xx][yy] > h:
            dfs(xx, yy, h)

if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    res = 0

    for h in range(100): #0-99까지의 높이
        ch = [[0] * n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0 and board[i][j] > h:
                    cnt += 1
                    dfs(i, j, h)
        res = max(res, cnt)
        if cnt == 0: #99까지 다 돌지 않도록 하기 위함
            break