#등산경로(DFS) 다시!
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def dfs(x,y):
    global cnt
    if x == ex and y == ey:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<n and 0<=yy<n and (board[xx][yy] > board[x][y]):
                if ch[xx][yy] == 0:
                    ch[xx][yy] = 1
                    dfs(xx,yy)
                    ch[xx][yy] = 0
if __name__ == '__main__':
    n = int(input())
    board = [[0]*n for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    max=-2147000000
    min=2147000000
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if tmp[j] < min:
                min = tmp[j]
                sx = i
                sy = j
            if tmp[j] > max:
                max = tmp[j]
                ex = i
                ey = j
            board[i][j] = tmp[j]#보드에 높이 입력
    ch[sx][sy] = 1 #최솟값부터 출발하기 때문에!
    cnt = 0
    dfs(sx, sy)
    print(cnt)
