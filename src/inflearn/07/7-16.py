#사다리타기(DFS)
def dfs(x, y):
    ch[x][y] = 1
    if x == 0:
        print(y)

    else:
        #왼쪽
        if y-1>0 and board[x][y-1] == 1 and ch[x][y-1] == 0:
            dfs(x,y-1)
        #오른쪽
        elif y+1<10 and board[x][y+1] == 1 and ch[x][y+1] == 0:
            dfs(x,y+1)
        #위쪽
        else:
            dfs(x-1, y)

if __name__ == '__main__':
    board = [list(map(int, input().split())) for _ in range(10)]
    ch = [[0]*10 for _ in range(10)]
    #도착지에서 출발
    #왼쪽, 오른쪽 먼저 본 후, 위쪽으로 이동
    #x:행번호, y:열번호
    for y in range(10):
        if board[9][y] == 2: #도착지
            dfs(9, y)